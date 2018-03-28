from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    #render the blog/post_list.html template with posts passed in as extra data
    return render(request, 'blog/post_list.html', {"posts":posts})

# this view is given pk as another param from urls.py (the regex named capture group)
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {"post":post})

def post_new(request):
    if request.method == "POST":
        #submitting form data
        form = PostForm(request.POST)
        if (form.is_valid()):
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        #display the form
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if (form.is_valid()):
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)    
    post.publish() #published method defined in Post model in models.py
    return redirect('post_detail', pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete() #each model has a delete method (by default)
    return redirect('post_list')


    