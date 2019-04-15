# Generated by Django 2.2 on 2019-04-15 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('day1', '0003_day11_day12_day13'),
    ]

    operations = [
        migrations.AddField(
            model_name='day11',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='day12',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='day13',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='day11',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
