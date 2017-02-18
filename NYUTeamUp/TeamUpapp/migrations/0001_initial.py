# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('appId', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jobId', models.CharField(max_length=25)),
                ('requirement', models.TextField()),
                ('timeStamp', models.DateTimeField()),
                ('numOfPositions', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('loginId', models.CharField(max_length=10)),
                ('userName', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('projectId', models.CharField(max_length=25)),
                ('projectName', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=25)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userId', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=50)),
                ('areaOfInterest', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=20)),
                ('emailId', models.EmailField(max_length=50)),
                ('loginId', models.ForeignKey(to='TeamUpapp.Login')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='userId',
            field=models.ForeignKey(to='TeamUpapp.User'),
        ),
        migrations.AddField(
            model_name='job',
            name='projectId',
            field=models.ForeignKey(to='TeamUpapp.Project'),
        ),
        migrations.AddField(
            model_name='application',
            name='jobId',
            field=models.ForeignKey(to='TeamUpapp.Job'),
        ),
        migrations.AddField(
            model_name='application',
            name='userId',
            field=models.ForeignKey(to='TeamUpapp.User'),
        ),
    ]
