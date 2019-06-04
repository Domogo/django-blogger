# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User  #AbstractUser
from django.db import models
import datetime
from django.utils import timezone
from django.conf import settings
from filer.fields.image import FilerImageField


class Profile(models.Model):
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		primary_key=True,
		)
	bio = models.CharField(max_length=500, blank=True)
	instagram = models.CharField(max_length=100, blank=True)
	fb = models.CharField(max_length=100, blank=True)
	website = models.CharField(max_length=100, blank=True)
	twitter = models.CharField(max_length=100, blank=True)
	following = models.PositiveIntegerField(default=0)
	followers = models.PositiveIntegerField(default=0)


class Blog(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	title = models.CharField(max_length=50, blank=False)
	cover = models.ImageField(null=True, blank=True, upload_to="media")
	info = models.CharField(max_length=200, blank=True)
	pub_date = models.DateTimeField('date published', blank=False)


class Post(models.Model):
    parent_blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50, blank=False)
    info = models.CharField(max_length=100000, blank=False)
    pub_date = models.DateTimeField('date published', blank=False)
    likes = models.PositiveIntegerField(default=0)


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='follower')
    followee = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='followee')


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)

class Images(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	image = models.ImageField(null=True, blank=True, upload_to="media/galery")
	image_width = models.PositiveIntegerField(null=True, blank=True)
	pub_date = models.DateTimeField('date published', blank=False, null=True)