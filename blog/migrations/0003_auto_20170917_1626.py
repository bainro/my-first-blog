# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 23:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='alt_text',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail_path',
            field=models.FilePathField(blank=True, default=None, null=True, path='/static/images/'),
        ),
    ]