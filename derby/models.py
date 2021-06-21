from django.db import models


# Create your models here.
class Derby(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    derby_type = models.CharField(max_length=100)
    no_entry = models.IntegerField()
    min_bet = models.FloatField()
    s_date = models.DateTimeField()
    e_date = models.DateTimeField()


class Entry(models.Model):
    tournament_id = models.IntegerField()
    user_id = models.IntegerField()
    owner = models.CharField(max_length=255)
    entry_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    is_member = models.BooleanField(default=False)
    member_id = models.IntegerField(default=0000)


class Fight(models.Model):
    tournament_id = models.IntegerField()
    user_id = models.IntegerField()
    owner_id = models.IntegerField()
    leg_band = models.CharField(max_length=255)
    wing_band = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    bet = models.FloatField()