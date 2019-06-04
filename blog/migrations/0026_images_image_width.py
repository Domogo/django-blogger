# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_images_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='image_width',
            field=models.PositiveIntegerField(default='700', null=True, editable=False, blank=True),
        ),
    ]
