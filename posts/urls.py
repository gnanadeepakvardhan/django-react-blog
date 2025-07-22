from django.urls import path
from .views import PostListView, PostDetailView, PostListAPI, PostDetailAPI, CommentListCreateAPI

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    # API endpoints
    path('api/posts/', PostListAPI.as_view(), name='api_post_list'),
    path('api/posts/<int:pk>/', PostDetailAPI.as_view(), name='api_post_detail'),
    path('api/posts/<int:post_pk>/comments/', CommentListCreateAPI.as_view(), name='api_post_comments'),
] 