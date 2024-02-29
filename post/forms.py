# posts/forms.py
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['author']  # Exclude author field from the form

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
