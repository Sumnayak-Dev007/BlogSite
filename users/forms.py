from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile



class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "w-full px-4 py-2 rounded-lg bg-gray-700 text-gray-100 border border-gray-600 "
                     "focus:outline-none focus:ring-2 focus:ring-indigo-500",

        })
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-4 py-2 rounded-lg bg-gray-700 text-gray-100 border border-gray-600 "
                     "focus:outline-none focus:ring-2 focus:ring-indigo-500",
        
        })
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-4 py-2 rounded-lg bg-gray-700 text-gray-100 border border-gray-600 "
                     "focus:outline-none focus:ring-2 focus:ring-indigo-500",
        
        })
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-700 text-gray-100 border border-gray-600 "
                         "focus:outline-none focus:ring-2 focus:ring-indigo-500",
            
            }),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["pic", "bio"]
        widgets = {
            "bio": forms.Textarea(attrs={
                "class": "w-full px-4 py-3 rounded-lg bg-gray-800 text-gray-100 border border-gray-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 resize-none",
                "placeholder": "Write a short bio...",
                "rows": 5,
            }),
            "pic": forms.FileInput(attrs={
                "class": "w-full text-sm file:bg-gray-700 file:text-gray-100 file:px-3 file:py-2 file:rounded file:border-0 file:cursor-pointer file:focus:outline-none",
                "id": "picUpload",
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['bio', 'pic']:
            self.fields[fieldname].help_text = None


        

