# Generated by Django 3.0.7 on 2020-07-03 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200703_2109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='billing_city',
            new_name='billing_town_or_city',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='shipping_city',
            new_name='shipping_town_or_city',
        ),
    ]