# Generated by Django 2.2.2 on 2019-11-28 05:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bbank', '0004_auto_20191128_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='LastDonated',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 28, 5, 51, 34, 203802, tzinfo=utc)),
        ),
    ]