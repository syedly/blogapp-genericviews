from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import blog, comment, faq, reply

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

class BlogForm(forms.ModelForm):
    class Meta:
        model = blog 
        exclude = ['user', 'like'] 
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['comment'] 
        
class FAQForm(forms.ModelForm):
    class Meta:
        model = faq
        fields = ['question']
        
class replyForm(forms.ModelForm):
    class Meta:
        model = reply
        fields = ['reply']