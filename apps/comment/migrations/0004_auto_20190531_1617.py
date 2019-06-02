# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-05-31 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_auto_20190531_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutcomment',
            name='is_read',
            field=models.BooleanField(default=False, verbose_name='是否已读'),
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='is_read',
            field=models.BooleanField(default=False, verbose_name='是否已读'),
        ),
        migrations.AddField(
            model_name='messagecomment',
            name='is_read',
            field=models.BooleanField(default=False, verbose_name='是否已读'),
        ),
    ]
