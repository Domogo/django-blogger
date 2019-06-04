# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171215_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fb',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
