# Generated by Django 4.2 on 2023-04-18 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_delete_userstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
