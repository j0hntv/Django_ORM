# Generated by Django 2.2.4 on 2020-04-11 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20200411_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='Flat',
            name='owner'
        ),
    migrations.RemoveField(
            model_name='Flat',
            name='owner_phone_pure'
        ),
    migrations.RemoveField(
            model_name='Flat',
            name='owners_phonenumber'
        )
    ]