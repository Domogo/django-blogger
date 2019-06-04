# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('blog', '0011_auto_20180129_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='cover',
            field=filer.fields.image.FilerImageField(related_name='blog_cover', to=settings.FILER_IMAGE_MODEL, null=True),
        ),
    ]
