"""Account forms file."""
from account.models import User
from account.tasks import send_activation_link_mail
from django import forms
from django.db import transaction
from django.utils.text import slugify


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
        send_activation_link_mail.apply_async(instance.id)
        return instance
