# Generated by Django 3.1 on 2020-10-19 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0020_auto_20201019_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='carTitle',
            field=models.ForeignKey(default='Выберите автомобиль', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.cartype', verbose_name='Название'),
        ),
    ]
