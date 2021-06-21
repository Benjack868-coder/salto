from django import forms
from django.contrib.auth.models import User
from django.core.validators import ValidationError, validate_email


class LoginForm(forms.Form):
    login_email = forms.CharField(max_length=255, initial='')
    system_password = forms.CharField()
    system_remember_me = forms.CheckboxInput()

    def clean_system_email(self):
        try:
            validate_email(self.cleaned_data.get('system_email'))
        except ValidationError as e:
            raise forms.ValidationError(e)


class RegistrationForm(forms.Form):
    system_firstname = forms.CharField(max_length=100, initial='')
    system_lastname = forms.CharField(max_length=100, initial='')
    system_email = forms.CharField(max_length=100, initial='')
    system_password = forms.CharField(max_length=100, initial='')
    system_password_confirm = forms.CharField(max_length=100, initial='')

    def clean(self):
        clean_data = super(RegistrationForm, self).clean()
        password1 = clean_data.get('system_password')
        password2 = clean_data.get('system_password_confirm')
        if not password1 == password2:
            raise forms.ValidationError('Password and Confirmation Password did not match.')

    def clean_system_email(self):
        email = self.cleaned_data.get('system_email')
        try:
            validate_email(email)
        except ValidationError as e:
            raise forms.ValidationError(e)
        else:
            try:
                User.objects.get(email=email).email
                raise forms.ValidationError('This email is already use by other.')
            except User.DoesNotExist:
                return email


class RecoverAccountForm(forms.Form):
    system_email = forms.CharField(max_length=100, initial='')