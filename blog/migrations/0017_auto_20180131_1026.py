# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20180131_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
