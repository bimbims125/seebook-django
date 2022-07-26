from atexit import register
from unicodedata import category
from django.contrib import admin
from .models import *
# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Books, BooksAdmin)
admin.site.register(Category, CategoryAdmin)