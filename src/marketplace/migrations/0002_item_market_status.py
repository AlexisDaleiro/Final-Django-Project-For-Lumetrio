# Generated by Django 4.2 on 2023-04-23 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='market_status',
            field=models.CharField(choices=[('sold', 'sold'), ('available', 'available')], default='available', max_length=20),
        ),
    ]
