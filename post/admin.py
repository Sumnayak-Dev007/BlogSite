from django.contrib import admin
from .models import Category, Catblog, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

# Custom form for Catblog to use CKEditor
class CatblogAdminForm(forms.ModelForm):
    descriptions = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Catblog
        fields = '__all__'

# Catblog admin
class CatblogAdmin(admin.ModelAdmin):
    form = CatblogAdminForm  # Use CKEditor in admin
    list_display = ('title', 'author', 'created_at')

# Register models
admin.site.register(Catblog, CatblogAdmin)
admin.site.register(Category)
admin.site.register(Comment)

