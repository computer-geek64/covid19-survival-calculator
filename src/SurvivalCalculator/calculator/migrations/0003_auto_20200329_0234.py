# Generated by Django 3.0.4 on 2020-03-29 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_auto_20200328_2148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='location',
            new_name='region',
        ),
    ]
