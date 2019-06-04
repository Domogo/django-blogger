# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20180131_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
