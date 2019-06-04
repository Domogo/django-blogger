# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20180131_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to='media/galery', blank=True)),
                ('user', models.ForeignKey(blank=True, to='blog.Profile', null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='cover',
            field=models.ImageField(null=True, upload_to='media', blank=True),
        ),
    ]
