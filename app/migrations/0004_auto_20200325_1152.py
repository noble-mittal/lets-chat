# Generated by Django 3.0.4 on 2020-03-25 11:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200325_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 3, 25, 11, 52, 20, 288292)),
        ),
    ]