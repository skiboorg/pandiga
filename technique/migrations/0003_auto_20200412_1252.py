# Generated by Django 2.1.4 on 2020-04-12 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technique', '0002_techniqueitem_rate_times'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techniquetype',
            name='image',
            field=models.ImageField(null=True, upload_to='technique/type/', verbose_name='Изображение (370 x 130)'),
        ),
    ]
