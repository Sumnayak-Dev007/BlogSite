from django import forms
from .models import Catblog, Comment
from django.utils.text import slugify
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
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
            'descriptions': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 rounded-lg bg-gray-700 text-gray-100 border border-gray-600 '
                         'focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none',
                'placeholder': 'Write your content here...',
                'rows': 4
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
            if Catblog.objects.filter(slug=slug).exists():
                raise ValidationError("This slug already exists. Please choose a unique slug.")
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
