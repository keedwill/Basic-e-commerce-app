# Generated by Django 2.2.6 on 2020-01-01 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20191222_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlist',
            name='product_name',
            field=models.CharField(default=False, max_length=20),
        ),
    ]
