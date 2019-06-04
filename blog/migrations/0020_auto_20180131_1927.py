# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_profile_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cover',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
