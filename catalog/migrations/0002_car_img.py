# Generated by Django 3.1 on 2020-09-01 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='../../media/images', verbose_name='Главная фотка'),
        ),
    ]
