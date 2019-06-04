# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20171223_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('info', models.CharField(max_length=100000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('parent_blog', models.ForeignKey(blank=True, to='blog.Blog', null=True)),
            ],
        ),
    ]
