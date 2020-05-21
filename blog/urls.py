from django.urls import path
from .views import BlogListView, BlogDetailView, add_comment_to_post

urlpatterns = [
    path('', BlogListView.as_view(), {'title': 'Blog'}, name='blog'),
    path('post/<int:pk>/', BlogDetailView.as_view(),
         {'title': 'Post'}, name='blog-post'),
    path('post/<int:pk>/comment/', add_comment_to_post,
         name='add_comment_to_post'),
]
