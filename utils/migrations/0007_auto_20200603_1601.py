# Generated by Django 3.0.5 on 2020-06-03 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0006_auto_20200601_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='cust_rule',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='price_disc',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
