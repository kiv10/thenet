from django.urls import path
from blog import views
from .import views
from .views import (
    PostListView,
    PostDetailView,
    PostcollabView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    FollowsListView,
    net,
    FollowersListView)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('net', net.as_view(), name='blog-net'),
   # path('user/<str:username>/follows', AListView.as_view(), name='blog-thefiles'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/', PostcollabView.as_view(), name='collab'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/del/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>/follows', FollowsListView.as_view(), name='user-follows'),
    path('user/<str:username>/followers', FollowersListView.as_view(), name='user-followers'),
]