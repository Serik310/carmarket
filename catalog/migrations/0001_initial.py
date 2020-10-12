# Generated by Django 3.1 on 2020-08-30 16:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carBrand', models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='Марка')),
                ('carModel', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Модель')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('cId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField(verbose_name='Год выпуска')),
                ('desc', models.TextField(blank=True, max_length=1500, null=True, verbose_name='Описание')),
                ('price', models.PositiveIntegerField()),
                ('engine', models.CharField(blank=True, choices=[('Diesel', 'Diesel'), ('Petrol', 'Petrol')], max_length=100, null=True, verbose_name='Тип Движка')),
                ('contact', models.CharField(blank=True, max_length=106, null=True, verbose_name='Номер телефона')),
                ('cStatus', models.CharField(blank=True, choices=[('S', 'SOLD'), ('N', 'NONE')], default='N', max_length=1, verbose_name='Статус')),
                ('date_publication', models.DateField(auto_now_add=True, null=True, verbose_name='Опубликовано')),
                ('mileage', models.PositiveIntegerField(verbose_name='Пробег')),
                ('city', models.CharField(blank=True, max_length=150, null=True, verbose_name='Город')),
                ('transmission', models.CharField(choices=[('M', 'Mechanics'), ('A', 'Auto')], default='M', max_length=1, verbose_name='КПП')),
                ('carTitle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.cartype', verbose_name='Полное название')),
            ],
        ),
    ]