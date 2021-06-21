from django.db import models

# Create your models here.


class Members(models.Model):
    user_id = models.CharField(max_length=10)
    owner = models.CharField(max_length=255)
    farm_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)

