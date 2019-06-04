# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_profile_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
