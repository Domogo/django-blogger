# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bio', models.TextField(max_length=500, blank=True)),
                ('instagram', models.TextField(max_length=100, blank=True)),
                ('fb', models.TextField(max_length=100, blank=True)),
                ('website', models.TextField(max_length=100, blank=True)),
                ('twitter', models.TextField(max_length=100, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
