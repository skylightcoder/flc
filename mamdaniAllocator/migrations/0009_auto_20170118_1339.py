# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-18 10:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mamdaniAllocator', '0008_auto_20161220_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='virtual_machine',
        ),
        migrations.DeleteModel(
            name='Server',
        ),
        migrations.DeleteModel(
            name='VirtualMachine',
        ),
    ]
