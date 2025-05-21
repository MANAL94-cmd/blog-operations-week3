from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='home'),  # Use profile view for homepage
    path('blog/', views.blog_list, name='blog_list'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('posts/<int:id>/edit/', views.edit_post, name='edit_post'),  # NEW
    path('about/', views.about_view, name='about'),
    path('post/<int:id>/delete/', views.delete_post, name='delete_post'),
]
