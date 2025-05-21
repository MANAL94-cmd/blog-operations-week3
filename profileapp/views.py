from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post

def about_view(request):
    return render(request, 'profileapp/about.html')

def profile(request):
    return render(request, 'profileapp/profile.html')

def blog_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'profileapp/blog_posts.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'profileapp/post_detail.html', {'post': post})

def home(request):
    return render(request, 'profileapp/home.html')

def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        post.title = title
        post.content = content
        post.save()
        
        messages.success(request, 'Post updated successfully!')
        return redirect('post_detail', id=post.id)
    
    return render(request, 'profileapp/edit_post.html', {'post': post})

def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('blog_list')

    return render(request, 'profileapp/confirm_delete.html', {'post': post})
