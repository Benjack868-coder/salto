from django import forms


class MemberRegistration(forms.Form):
    owner = forms.CharField(max_length=255, initial='')
    farm_name = forms.CharField(max_length=255, initial='')
    location = forms.CharField(max_length=255, initial='')
    email = forms.CharField(max_length=255, initial='')
    contact_number = forms.CharField(max_length=255, initial='')

