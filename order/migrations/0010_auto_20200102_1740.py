# Generated by Django 2.2.6 on 2020-01-02 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_auto_20200102_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlist',
            name='product_price',
            field=models.IntegerField(),
        ),
    ]
