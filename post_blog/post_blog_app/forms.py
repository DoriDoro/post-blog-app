from django import forms
from .models import Post, Todo

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'body']

class TodoForm(forms.ModelForm):
    model = Todo
    fields = ['title', 'body', 'is_done']
