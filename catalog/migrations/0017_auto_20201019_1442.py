# Generated by Django 3.1 on 2020-10-19 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_remove_car_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='cId',
        ),
        migrations.AddField(
            model_name='car',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]