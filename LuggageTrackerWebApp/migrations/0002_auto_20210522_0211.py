# Generated by Django 3.2.3 on 2021-05-22 02:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LuggageTrackerWebApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='luggage',
            name='digital_signature',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Disapproved', 'Disapproved'), ('Waiting', 'Waiting')], default='Waiting', max_length=20),
        ),
        migrations.AddField(
            model_name='luggage',
            name='flagged',
            field=models.CharField(choices=[('N', 'N'), ('Y', 'Y')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='luggage',
            name='status',
            field=models.CharField(choices=[('Arrived', 'Arrived'), ('In Transit', 'In Transit')], default='n/a', max_length=20),
        ),
        migrations.AlterField(
            model_name='luggage',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 22, 2, 11, 41, 584280), verbose_name='Time Last Scanned'),
        ),
    ]
