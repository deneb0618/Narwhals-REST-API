# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-13 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('narwhals', '0008_auto_20170129_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swimworkout',
            name='distance',
            field=models.FloatField(default=0, help_text='Distance of the training', verbose_name='Distance of the training'),
        ),
        migrations.AlterField(
            model_name='swimworkout',
            name='duration',
            field=models.IntegerField(default=0, help_text='Duration of the training', verbose_name='Duration of the training'),
        ),
        migrations.AlterField(
            model_name='swimworkout',
            name='strokes',
            field=models.FloatField(default=0, help_text='Calculated strokes', verbose_name='Calculated strokes'),
        ),
    ]
