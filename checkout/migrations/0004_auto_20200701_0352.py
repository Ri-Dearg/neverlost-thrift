# Generated by Django 3.0.7 on 2020-07-01 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20200628_0450'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_bag',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]
