# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='post_liked',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user_liked',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
