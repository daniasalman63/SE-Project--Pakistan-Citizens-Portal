# Generated by Django 4.0.7 on 2023-04-05 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_account_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='cnic',
            new_name='CNIC',
        ),
    ]
