# Generated by Django 2.1.4 on 2020-03-05 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('technique', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='techniqueitem',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='technique.TechniqueSection', verbose_name='Относится к разделу'),
        ),
        migrations.AddField(
            model_name='techniqueitem',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='technique.TechniqueType', verbose_name='Относится к типу'),
        ),
    ]