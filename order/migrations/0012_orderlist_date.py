# Generated by Django 2.2.6 on 2020-01-03 21:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_auto_20200102_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlist',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]