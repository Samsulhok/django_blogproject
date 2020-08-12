from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
	list_diplay = ('title', 'content')

admin.site.register(Blog, BlogAdmin)
