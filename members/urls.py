from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, PassWordSuccess, ShowProfilePagelView, EditProfilePagelView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    # path('password/', auth_views.PasswordChangeView.as_view(
    #     template_name='registration/change-password.html'), )
    path('password/', PasswordsChangeView.as_view()),
    path('password_success/', PassWordSuccess, name='password_success'),
    path('<int:pk>/profile/', ShowProfilePagelView.as_view(),
         name='show_profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePagelView.as_view(),
         name='edit_profile_page'),
]
