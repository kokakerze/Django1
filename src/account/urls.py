"""Register account urls."""
from account import views
from django.urls import path


app_name = "account"

urlpatterns = [
    path('my_profile', views.MyProfile.as_view(), name="my_profile")
]
