from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),  # Profile page
    path('blog/', views.blog_list, name='blog_list'),  # Blog list page
    path('blog/post/<int:id>/', views.blog_detail, name='post_detail'),  # Blog post detail page
]
