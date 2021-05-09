from django.urls import path
from account import views


app_name = "account"

urlpatterns = [
    path('my_profile/<int:pk>', views.MyProfile.as_view(), name="my_profile")
]
