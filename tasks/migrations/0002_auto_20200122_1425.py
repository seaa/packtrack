# Generated by Django 2.2.5 on 2020-01-22 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='accidental_delivery_duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='task',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='task',
            name='assignee',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='task',
            name='delay',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='task',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='task',
            name='end_time',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='latitude',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='task',
            name='longitude',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='task',
            name='request_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='task',
            name='start_time',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
