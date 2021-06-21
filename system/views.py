from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
# salto project class
from .forms import LoginForm, RegistrationForm


class Index(View):
    def get(self, request, **kwargs):
        print(request.user.is_authenticated)
        return render(request, 'system/index.html', {})


class Login(View):
    template_name = 'system/login.html'
    context = {}
    form = LoginForm()

    def get(self, request, **kwargs):
        self.context = {'form': self.form}
        return render(request, template_name=self.template_name, context=self.context)

    def post(self, request, **kwargs):
        self.form = LoginForm(request.POST)
        self.context = {'form': self.form}
        if self.form.is_valid():
            email = self.form.cleaned_data.get('login_email')
            password = self.form.cleaned_data.get('system_password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                pass
                login(request, user)
                return redirect('system_index')
            else:
                self.context['login_error'] = 'Please enter the correct username and password. Note that both fields may be case-sensitive.'
        return render(request, template_name=self.template_name, context=self.context)


class Register(View):
    template_name = 'system/register.html'
    context = {}
    form = RegistrationForm()

    def get(self, request, **kwargs):
        return render(request, template_name=self.template_name,context=self.context)

    def post(self, request, **kwargs):
        self.form = RegistrationForm(request.POST)
        self.context['form'] = self.form
        if self.form.is_valid():
            try:
                form = self.form
                firstname = form.cleaned_data.get('system_firstname')
                lastname = form.cleaned_data.get('system_lastname')
                email = form.cleaned_data.get('system_email')
                password = make_password(self.form.cleaned_data.get('system_password'), salt=None, hasher='default')
                user = User(username=email, email=email, password=password, first_name=firstname, last_name=lastname)
                user.save()
                self.context['form'] = {}
                self.context['registered'] = True
            except User.DoesNotExist:
                pass
        return render(request, template_name=self.template_name, context=self.context)


class Recover(View):
    template_name = 'system/recover.html'
    form = {}
    context = {}

    def get(self, request, **kwargs):
        return render(request, template_name=self.template_name, context=self.context)


def signout(request):
    logout(request)
    return redirect('system_login')