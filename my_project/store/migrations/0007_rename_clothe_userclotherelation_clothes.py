# Generated by Django 4.1.4 on 2023-01-23 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_userclothebookrelation_userclotherelation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userclotherelation',
            old_name='clothe',
            new_name='clothes',
        ),
    ]
