# Generated by Django 3.1.7 on 2021-03-06 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('derby', '0002_entry_is_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='member_id',
            field=models.IntegerField(default=0),
        ),
    ]
