from django.contrib import admin
from gallery.models import GALLERY
from blog.models import Blog
# Register your models here.

# 注册model
admin.site.register(GALLERY)
admin.site.register(Blog)
