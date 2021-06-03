"""Manage information that shows in urls for account."""
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView

from .forms import UserRegisterForm
from .models import User


# Create your views here.


class MyProfile(LoginRequiredMixin, UpdateView):
    """Update profiles."""

    queryset = User.objects.filter(is_active=True)
    fields = ("first_name", "last_name",)
    success_url = reverse_lazy("homepage")

    def get_object(self, queryset=None):
        """Get user from request."""
        return self.request.user


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

    def get(self, request, confirmation_token):
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
