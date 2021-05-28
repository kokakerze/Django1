"""Register account urls."""
from account import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path

app_name = "account"

urlpatterns = [
    path('my_profile/', views.MyProfile.as_view(), name="my_profile"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('activate/<str:confirmation_token>', views.ActivateUserView.as_view(), name="activate"),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name="account/login.html"), name='login'),
]
