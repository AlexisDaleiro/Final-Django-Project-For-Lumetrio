# Generated by Django 4.2 on 2023-04-24 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0007_marketcommunication_email_marketcommunication_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketcommunication',
            name='email',
            field=models.EmailField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='marketcommunication',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
