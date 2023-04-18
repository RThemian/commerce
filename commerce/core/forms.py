from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'your username',
        'class': 'w-full py-4 px-6 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500'
        }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'your email address',
        'class': 'w-full py-4 px-6 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500'
        }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'your password',
        'class': 'w-full py-4 px-6 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500'
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'confirm your password',
        'class': 'w-full py-4 px-6 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500'
        }))
    