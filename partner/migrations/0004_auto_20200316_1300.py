# Generated by Django 2.1.4 on 2020-03-16 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0003_auto_20200316_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parnter',
            name='total_earned',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Всего начислено'),
        ),
        migrations.AlterField(
            model_name='partnermoney',
            name='action',
            field=models.CharField(blank=True, default=0, max_length=10, null=True, verbose_name='Операция'),
        ),
    ]