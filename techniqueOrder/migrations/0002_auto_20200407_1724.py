# Generated by Django 2.1.4 on 2020-04-07 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techniqueOrder', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='techniqueorderviewed',
            options={'verbose_name': 'Просмотры заявок', 'verbose_name_plural': 'Просмотры заявок'},
        ),
        migrations.AddField(
            model_name='techniqueorder',
            name='customer_feedback',
            field=models.BooleanField(default=False, verbose_name='Отзыв от заказчика'),
        ),
        migrations.AddField(
            model_name='techniqueorder',
            name='worker_feedback',
            field=models.BooleanField(default=False, verbose_name='Отзыв от исполнителя'),
        ),
    ]