# Generated by Django 3.2.5 on 2021-08-03 05:08

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_client_operation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discount',
            options={'ordering': ('order_num',), 'verbose_name': 'Скидка', 'verbose_name_plural': 'Скидки'},
        ),
        migrations.RemoveField(
            model_name='review',
            name='name',
        ),
        migrations.AddField(
            model_name='discount',
            name='discount_deadline',
            field=models.DurationField(default=datetime.timedelta(0), verbose_name='Срок действия купона'),
        ),
        migrations.AddField(
            model_name='operation',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operation',
            name='status',
            field=models.CharField(choices=[('1', 'Активирован'), ('2', 'Неактивирован'), ('3', 'Просрочен')], default=1, max_length=255, verbose_name='Статус операции'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.client'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='client_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя пользователя'),
        ),
        migrations.AddField(
            model_name='review',
            name='discount',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.discount'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='discount',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='core.company'),
        ),
        migrations.AlterField(
            model_name='location',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='core.company'),
        ),
    ]
