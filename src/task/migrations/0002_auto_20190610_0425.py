# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-06-10 04:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='due_date',
            field=models.DateField(null=True),
        ),
    ]
