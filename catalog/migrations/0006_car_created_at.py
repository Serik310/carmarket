# Generated by Django 3.1 on 2020-09-05 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20200901_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='created_at',
            field=models.DateField(auto_now=True, verbose_name='Дата создания'),
        ),
    ]
