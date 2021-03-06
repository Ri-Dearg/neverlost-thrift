# Generated by Django 3.0.7 on 2020-07-04 11:03

from django.db import migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200704_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='billing_phone_number',
            field=users.models.CustomPhoneNumberField(blank=True, default='', max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='shipping_phone_number',
            field=users.models.CustomPhoneNumberField(blank=True, default='', max_length=128, region=None),
        ),
    ]
