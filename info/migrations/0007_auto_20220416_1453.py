# Generated by Django 3.1 on 2022-04-16 05:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_event_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.AddField(
            model_name='event',
            name='date_end',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='終了日'),
        ),
        migrations.AddField(
            model_name='event',
            name='date_start',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='開催日'),
        ),
    ]
