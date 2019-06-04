# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_blog_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('followee', models.ForeignKey(related_name='followee', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('follower', models.ForeignKey(related_name='follower', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
