from django import forms


class DerbyRegistration(forms.Form):
    name = forms.CharField(max_length=100, initial='')
    location = forms.CharField(max_length=100, initial='')
    derby_type = forms.CharField(max_length=100, initial='')
    no_entry = forms.IntegerField()
    min_bet = forms.CharField(max_length=100, initial='')
    s_date = forms.CharField(max_length=100, initial='')
    e_date = forms.CharField(max_length=100, initial='')


class EntryRegistration(forms.Form):
    tournament_id = forms.CharField(max_length=100, initial='')
    member_id = forms.CharField(max_length=100, initial=0)
    owner = forms.CharField(max_length=100, initial='')
    entry_name = forms.CharField(max_length=100, initial='')
    email = forms.CharField(max_length=100, initial='')
    contact_number = forms.CharField(max_length=100, initial='')



class FightRegistration(forms.Form):
    leg_band = forms.CharField(max_length=100, initial='')
    wing_band = forms.CharField(max_length=100, initial='')
    weight = forms.CharField(max_length=100, initial='')
    bet = forms.FloatField(initial='1000')