# Generated by Django 2.2.6 on 2020-01-13 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_auto_20200104_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlist',
            name='unit_cost',
            field=models.IntegerField(default=False),
        ),
    ]
