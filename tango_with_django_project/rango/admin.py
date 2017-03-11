'''
Created on Mar 10, 2017

@author: jackwang
'''
from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes', 'level')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)

