from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from blogapp.models import Profile


class CreateProfilePageView(CreateView):
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile_page.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePagelView(UpdateView):
    model = Profile
    template_name = "registration/edit_profile_page.html"
    fields = ['bio', 'profile_img', 'website_url',
              'facebook_url', 'twitter_url', 'instagram_url']
    success_url = reverse_lazy('list')


class ShowProfilePagelView(DetailView):
    model = Profile
    template_name = "registration/user_profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePagelView,
                        self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user

        return context


class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')


class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy('list')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = "registration/change-password.html"
    success_url = reverse_lazy('password_success')


def PassWordSuccess(request):
    return render(request, 'registration/password_success.html', {})
