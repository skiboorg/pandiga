# Generated by Django 2.2.7 on 2020-04-28 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='Город')),
                ('region', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='Регион')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города и регионы',
            },
        ),
    ]
