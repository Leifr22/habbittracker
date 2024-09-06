from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from users.forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm


# Create your views here.


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'user/login.html'
    extra_content={'title':'Авторизация'}
    def get_success_url(self):
        return reverse_lazy('login')
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('login')
    extra_content = {'title': 'Регистрация'}
def register(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'user/register_done.html')
        else:
            form = RegisterUserForm()
    return render(request, 'user/register.html', {'form': form})
class ProfileUser(UpdateView):
    models = get_user_model()
    form_class = ProfileUserForm
    template_name = 'user/profile.html'
    extra_content ={'title':'Профиль'}
    def get_success_url(self):
        return reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user
class ChangePassword(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name ='user/password_change_form.html'
    success_url = reverse_lazy('password_change_done')






