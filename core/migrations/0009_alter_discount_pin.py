# Generated by Django 3.2.5 on 2021-08-04 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210803_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='pin',
            field=models.CharField(default=3374, max_length=4, verbose_name='Пин-код'),
        ),
    ]
