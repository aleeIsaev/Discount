# Generated by Django 3.2.5 on 2021-08-05 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_company_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='status',
            field=models.CharField(choices=[('1', 'Активирован'), ('2', 'Забронированн'), ('3', 'Просрочен')], default='2', max_length=255, verbose_name='Статус операции'),
        ),
    ]