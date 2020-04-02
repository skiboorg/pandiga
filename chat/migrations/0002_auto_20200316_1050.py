# Generated by Django 2.1.4 on 2020-03-16 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chat', '0001_initial'),
        ('techniqueOrder', '0001_initial'),
        ('technique', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Сообщение от'),
        ),
        migrations.AddField(
            model_name='chat',
            name='lastMsgBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Сообщение от'),
        ),
        migrations.AddField(
            model_name='chat',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='techniqueOrder.TechniqueOrder', verbose_name='Тема чата заявка'),
        ),
        migrations.AddField(
            model_name='chat',
            name='techniqueitem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='technique.TechniqueItem', verbose_name='Тема чата техника'),
        ),
        migrations.AddField(
            model_name='chat',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='chatusers', to=settings.AUTH_USER_MODEL, verbose_name='Пользователи'),
        ),
    ]