# Generated by Django 3.2.3 on 2021-05-20 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LuggageTrackerWebApp', '0005_alter_luggageblockchain_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='luggageblockchain',
            old_name='prev_id',
            new_name='prev_hash_id',
        ),
        migrations.AddField(
            model_name='luggageblockchain',
            name='destination_airport',
            field=models.CharField(choices=[('ORD', 'CHICAGO/ORD'), ('EWR', 'NEWARK/EWR')], default='', max_length=3),
        ),
        migrations.AddField(
            model_name='luggageblockchain',
            name='digital_signature',
            field=models.CharField(choices=[('NA', 'AWAITING SIGNTURE'), ('C', 'CHECKED IN'), ('IT', 'IN TRANSIT'), ('R', 'REACHED DESTINATION'), ('M', 'MISSING'), ('D', 'DELAYED'), ('BC', 'BAGGAGE CLAIM'), ('A', 'RETRIVED BY CUSTOMER'), ('E', 'CHECK MEMO FOR ERROR')], default='NA', max_length=2),
        ),
        migrations.AddField(
            model_name='luggageblockchain',
            name='flagged',
            field=models.CharField(choices=[('Y', 'YES'), ('N', 'NO')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='luggageblockchain',
            name='memo',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AddField(
            model_name='luggageblockchain',
            name='name',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AddField(
            model_name='luggageblockchain',
            name='origin_airport',
            field=models.CharField(choices=[('ORD', 'CHICAGO/ORD'), ('EWR', 'NEWARK/EWR')], default='', max_length=3),
        ),
    ]