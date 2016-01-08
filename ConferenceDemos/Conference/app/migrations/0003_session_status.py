# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151229_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='status',
            field=models.CharField(choices=[('a', 'Approved'), ('s', 'Submitted'), ('r', 'Rejected')], default='s', max_length=1),
            preserve_default=False,
        ),
    ]
