# Generated by Django 3.1 on 2020-10-12 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_auto_20200927_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='slug',
        ),
    ]
