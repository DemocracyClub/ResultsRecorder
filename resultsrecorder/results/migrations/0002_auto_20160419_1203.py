# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 12:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultset',
            name='ip_address',
            field=models.GenericIPAddressField(default='127.0.0.1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidateresult',
            name='is_winner',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='resultset',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='result_sets', to=settings.AUTH_USER_MODEL),
        ),
    ]
