"""Account forms file."""
from django import forms
from django.contrib.auth.forms import UsernameField, ReadOnlyPasswordHashField, UserChangeForm
from django.db import transaction
from django.utils.text import slugify


from account.models import User, Avatar
from account.tasks import send_activation_link_mail


class UserRegisterForm(forms.ModelForm):
    """Create form for registration user."""

    password = forms.CharField(widget=forms.PasswordInput)
    confirmation_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        """Meta class to sets fields to Form."""

        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'confirmation_password')

    def clean(self):
        """Check clean of information in forms."""
        clean_data: dict = super().clean()
        """Here is location of our form (breakpoint for checking in next line)."""
        if clean_data['password'] != clean_data['confirmation_password']:
            self.add_error('password', 'Password mismatch!')
            # raise forms.ValidationError("Password mismatch!")
            """Alternatively error in forms not in fields."""

        if not clean_data['username']:
            clean_data['username'] = slugify(clean_data['first_name'])
        return clean_data

    def clean_email(self):
        """Check email for clean inputting."""
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=email).exists():
            self.add_error('email', 'Email already exists!')
        return email

    @transaction.atomic
    def save(self, commit=True):
        """Save in transaction method and sends mail."""
        instance: User = super().save(commit=False)
        """Variable instance is our model, named User."""
        instance.is_active = False
        instance.set_password(self.cleaned_data["password"])
        instance.save()
        """Making send mail not in view, cause in view User dont have id."""
        send_activation_link_mail.apply_async(agrs=[instance.id], countdown=10)
        return instance


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ("file_path",)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)

    def save(self, commit=False):
        instance = super().save(commit=False)
        instance.user = self.request.user
        instance.save()
        return instance


class ProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": 'form-control', "placeholder": "Ваш имейл"}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class": 'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class": 'form-control'}))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class": 'form-control'}))

    password = ReadOnlyPasswordHashField(
        label=("Password"),
        help_text=(
            'Raw passwords are not stored, so there is no way to see this '
            'user’s password, but you can change the password using '
            '<a href="{}">this form</a>.'
        ),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password',)
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get('password')
        if password:
            password.help_text = password.help_text.format('../password/')
        user_permissions = self.fields.get('user_permissions')
        if user_permissions:
            user_permissions.queryset = user_permissions.queryset.select_related('content_type')

    def clean_password(self):
        return self.initial.get('password')

    def save(self, commit=False):
        instance = super().save(commit=False)
        instance.user = self.request.user
        instance.save()
        return instance
