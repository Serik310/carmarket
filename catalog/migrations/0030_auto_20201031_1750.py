# Generated by Django 3.1 on 2020-10-31 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0029_auto_20201028_1659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='data_order',
            new_name='date_ordered',
        ),
    ]
