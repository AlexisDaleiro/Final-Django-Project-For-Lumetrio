# Generated by Django 4.2 on 2023-04-18 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_userstatus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userstatus',
            old_name='last_active',
            new_name='is_active',
        ),
    ]
