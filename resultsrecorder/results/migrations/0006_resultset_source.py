# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0005_resultset_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultset',
            name='source',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]