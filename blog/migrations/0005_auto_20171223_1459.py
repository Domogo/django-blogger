# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='info',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
