# Generated by Django 3.1 on 2020-09-06 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20200905_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='slug',
            field=models.SlugField(default='cardet'),
            preserve_default=False,
        ),
    ]
