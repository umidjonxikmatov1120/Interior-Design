from django.contrib import admin

from pages.models import *


@admin.register(AboutModel)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['title', 'description']
    search_fields = ['title']


@admin.register(ImagesModel)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['title', 'description']
    search_fields = ['title']


@admin.register(ServiceModel)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['title', 'description']
    search_fields = ['title']


@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'likes', 'comments']
    list_filter = ['title', 'likes']
    search_fields = ['title', 'comments']


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']
    list_filter = ['name', 'email']
    search_fields = ['name', 'email']