from django.contrib import admin
from .models import Category, Catblog,Comment

class CatblogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at') 

admin.site.register(Catblog, CatblogAdmin)
admin.site.register(Category)
admin.site.register(Comment)
