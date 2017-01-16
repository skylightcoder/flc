# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mamdaniAllocator', '0006_outputset'),
    ]

    operations = [
        migrations.CreateModel(
            name='outputfunction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_index', models.FloatField(default=0)),
                ('EMPTY', models.IntegerField(default=0)),
                ('ALMOSTEMPTY', models.IntegerField(default=0)),
                ('MEDIUM', models.IntegerField(default=0)),
                ('ALMOSTFULL', models.IntegerField(default=0)),
                ('FULL', models.IntegerField(default=0)),
            ],
        ),
    ]