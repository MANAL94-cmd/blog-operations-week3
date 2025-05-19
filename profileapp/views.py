from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def profile(request):
    
    return render(request, 'profileapp/profile.html')

def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'profileapp/blog_posts.html', {'posts': posts})

def blog_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'profileapp/blog_detail.html', {'post': post})


