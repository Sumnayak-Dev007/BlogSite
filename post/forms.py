from django import forms
from .models import Catblog, Comment
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostForm(forms.ModelForm):
    descriptions = forms.CharField(
        widget=CKEditorUploadingWidget(config_name='default', attrs={
        'class': 'md:w-[100%] w-[100%] px-4 py-2 bg-gray-700 text-gray-100 border rounded-lg border-gray-600 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none',  # forces editor iframe body bg/text color
    })
     )
    
    class Meta:
        model = Catblog
        fields = ['category','slug','title','blog_image','descriptions']

        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full px-4 py-2 rounded-lg bg-gray-700 text-gray-100 border border-gray-600 '
                         'focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none',
            }),
            'slug': forms.TextInput(attrs={
                'class': (
                    'w-full px-4 py-2 rounded-lg bg-gray-700 text-gray-100 border border-gray-600 '
                    'focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none'
                ),
                'placeholder': 'Enter unique slug (e.g., my-awesome-post)'
            }),
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 rounded-lg bg-gray-700 text-gray-100 border border-gray-600 '
                         'focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none',
                'placeholder': 'Enter title'
            }),
            'blog_image': forms.ClearableFileInput(attrs={
                'class': (
                    'w-full text-gray-100 '
                    'file:mr-4 file:py-2 file:px-4 '
                    'file:rounded-lg file:border-1 '
                    'file:text-sm file:font-semibold '
                    'file:bg-gray-700 file:text-gray-200 '
                    'hover:file:bg-gray-600 cursor-pointer'
                )
            }),
            
        }

    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        if slug:
            slug = slugify(slug)  # convert to lowercase, replace spaces with dashes
            # Check if the slug already exists in the database
            if Catblog.objects.filter(slug=slug).exclude(id=self.instance.id).exists():
                raise ValidationError("This slug already exists. Type in a unique slug.")
        return slug


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': '💬 Share your thoughts...',
            'class': (
                'w-full px-4 py-3 rounded-lg '
                'bg-gray-800 text-gray-100 border border-gray-700 '
                'focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 '
                'placeholder-gray-400 resize-none'
            )
        })
    )
    class Meta:
        model = Comment
        fields = ['content']
