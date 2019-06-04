# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_images_image_width'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image_width',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
