# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='f_email',
            field=models.TextField(null='false'),
        ),
    ]
