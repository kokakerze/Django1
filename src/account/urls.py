"""Register account urls."""
from account import views
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy


app_name = "account"

urlpatterns = [
    path('my_profile/edit/', views.Editsettings.as_view(), name="my_profile"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('activate/<str:confirmation_token>', views.ActivateUserView.as_view(), name="activate"),
    path('password/', views.change_password, name='change_password'),
    path('logout', views.logout, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name="account/login.html", redirect_authenticated_user=True),
         name='login'),
    path('reset/', auth_views.PasswordResetView.as_view(template_name="account/password_reset.html",
                                                        email_template_name='account/password_reset_email.html',
                                                        subject_template_name='account/password_reset_subject.txt',
                                                        success_url=reverse_lazy('account:password_reset_done')),
         name='password_reset'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html",
                                                     success_url=reverse_lazy('account:password_reset_complete')),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_complete.html"),
         name='password_reset_complete'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_done.h tml"),
         name='password_reset_done'),
    path('my_profile/ava/create/', views.AvaCreateView.as_view(), name='my_profile_ava_create'),
    path('my_profile/ava/list', views.AvaListView.as_view(), name='my_profile_ava_list'),
    path('<int:pk>/my_profile/', views.ShowProfilePageView.as_view(), name="show_profile_page"),
    path('<int:pk>/edit_profile/', views.EditProfilePageView.as_view(), name="edit_profile_page"),
    path('create_profile/', views.CreateProfileView.as_view(), name="create_profile_page"),

]
