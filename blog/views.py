from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    #render the blog/post_list.html template with posts passed in as extra data
    return render(request, 'blog/post_list.html', {"posts":posts})

# this view is given pk as another param from urls.py (the regex named capture group)
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {"post":post})

