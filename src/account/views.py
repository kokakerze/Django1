"""Manage information that shows in urls for account."""
from account.forms import AvatarForm, ProfileForm, ProfilePageForm, UserRegisterForm
from account.models import Avatar, Profile, User
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, UpdateView


class ShowProfilePageView(DetailView):
    """Show profile View."""

    model = Profile
    template_name = 'account/user_profile.html'
    queryset = Avatar.objects.all()

    def get_context_data(self, *args, **kwargs):
        """Return context data for Profile."""
        # avatar = Avatar.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

    def get_object(self, queryset=None):
        """Get user from request."""
        return self.request.user

    def get_queryset(self):
        """Get queryset and return filtered list."""
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class Editsettings(LoginRequiredMixin, UpdateView):
    """Update profile settings."""

    form_class = ProfileForm
    # queryset = User.objects.filter(is_active=True)
    # fields = ("first_name", "email")
    success_url = reverse_lazy("homepage")

    def get_object(self, queryset=None):
        """Get user from request."""
        return self.request.user


class CreateProfileView(CreateView):
    """Create Profile for user just created."""

    model = Profile
    form_class = ProfilePageForm
    template_name = "account/create_user_profile_page.html"

    def form_valid(self, form):
        """Make user profile valuable to the form."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageView(LoginRequiredMixin, UpdateView):
    """Edit profile page for user."""

    model = Profile
    template_name = "account/edit_profile_page.html"
    fields = ['bio', 'profile_picture', 'website_url', 'facebook_url', 'instagram_url', 'twitter_url']
    success_url = reverse_lazy("homepage")


class SignUpView(CreateView):
    """Creates class for singing up views."""

    model = User
    form_class = UserRegisterForm
    template_name = "account/user_signup.html"
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        """Check form for validation."""
        print(SignUpView)
        return super().form_valid(form)


class ActivateUserView(View):
    """Make User active after email confirmation."""

    @staticmethod
    def get(request, confirmation_token):
        """Get User and make it active."""
        user = get_object_or_404(User, confirmation_token=confirmation_token)
        user.is_active = True
        user.save(update_fields=('is_active',))
        return redirect("homepage")


def change_password(request):
    """Change password for current User."""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            print("Form is valid!")
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Ваш пароль был сохранен!')
            return redirect('homepage')
        else:
            print("Form not valid!")
            messages.error(request, 'Исправльте ошибку.')
    else:
        print("Else")
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {
        'form': form
    })


def logout(request):
    """Logout current user."""
    auth_logout(request)
    return redirect("homepage")


class AvaCreateView(LoginRequiredMixin, CreateView):
    """Create Avatar View."""

    model = Avatar
    form_class = AvatarForm
    success_url = reverse_lazy("homepage")

    # def get_form(self, form_class=None):
    #     """Return an instance of the form to be used in this view."""
    #     if form_class is None:
    #         form_class = self.get_form_class()
    #     return form_class(request=self.request, **self.get_form_kwargs())

    def get_form_kwargs(self):
        """Return super kwargs."""
        super_kwargs = super().get_form_kwargs()
        super_kwargs["request"] = self.request
        return super_kwargs


class AvaListView(LoginRequiredMixin, ListView):
    """Create User Profile Picture List."""

    queryset = Avatar.objects.all()

    def get_queryset(self):
        """Take queryset from Avatar."""
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    # def get_queryset(self):
    #     return self.request.user.avatar_set.all()
