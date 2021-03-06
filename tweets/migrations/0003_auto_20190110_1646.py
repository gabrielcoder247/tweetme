# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-01-10 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import tweets.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_auto_20190109_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(max_length=140, validators=[tweets.validators.validate_content]),
        ),
    ]
