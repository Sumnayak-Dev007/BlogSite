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