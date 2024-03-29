# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

# Register your models here.
class ProfileInLine(admin.StackedInline):
	model = Profile



admin.site.register(Profile)
admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(Like)
admin.site.register(Images)
