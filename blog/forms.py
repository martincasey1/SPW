from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.db.models import fields
from .models import Comment, Gallery, Contact


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {

            #'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'})
        }
  
class galleryForm(forms.ModelForm):
  
    class Meta:
        model = Gallery
        fields = ['name', 'gallery_Main_Img']      
   
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email_address', 'message']
        
        widgets = {

            'message' : forms.Textarea, 

        }
