# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mamdaniAllocator', '0004_cpuset'),
    ]

    operations = [
        migrations.CreateModel(
            name='diskset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SMALL', models.FloatField(default=0)),
                ('MEDIUM', models.FloatField(default=0)),
                ('LARGE', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ramset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SMALL', models.FloatField(default=0)),
                ('MEDIUM', models.FloatField(default=0)),
                ('LARGE', models.FloatField(default=0)),
            ],
        ),
    ]
