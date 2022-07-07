from django.shortcuts import render
from .models import Post, Todo
from .forms import PostForm, TodoForm

def base(request):
    return render(request, 'base.html', {})

def posts_list(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            form.save()
            posts = Post.objects.all()
            return render(request, 'posts.html', {'posts': posts})
        else:
            posts = Post.objects.all()
            return render(request, 'posts.html', {'posts': posts})

    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def todos_list(request):
    todos = Todo.objects.all()
    return render(request, 'todos.html', {'todos': todos})

