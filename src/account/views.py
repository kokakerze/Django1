"""Manage information that shows in urls for account."""
from account.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

# Create your views here.


class MyProfile(LoginRequiredMixin, UpdateView):
    """Update profiles."""

    queryset = User.objects.filter(is_active=True)
    fields = ("first_name", "last_name",)
    success_url = reverse_lazy("homepage")

    def get_object(self, queryset=None):
        """Get user from request."""
        return self.request.user
