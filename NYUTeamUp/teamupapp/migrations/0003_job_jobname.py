# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamupapp', '0002_remove_job_jobname'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='jobName',
            field=models.CharField(default='', max_length=50),
        ),
    ]
