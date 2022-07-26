from turtle import textinput

from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from core.models import *

class AddBookForms(ModelForm):
    class Meta:
        model = Books
        exclude = ['slug']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'required':True, 'placeholder':'Input book title'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'required':True, 'placeholder':'Input author name'}),
            'category':forms.Select(attrs={'class':'form-control', 'required':True}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'file': forms.FileInput({'class':'form-control'}),
            'cover':forms.FileInput({'class':'form-control'})
        }
        # title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'required':True, 'placeholder':'Input book title'}))
        # author = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'required':True, 'placeholder':'Input Author name'}))
        # category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select({'class':'form-control', 'required':True}) )
        # description = forms.CharField(widget=forms.Textarea({'class':'form-control'}))
        # cover = forms.ImageField(widget=forms.FileInput({'class':'form-control', 'required':True}))
        # file = forms.FileField(widget=forms.FileInput({'class':'form-control', 'required':True}))