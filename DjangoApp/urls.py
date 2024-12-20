from django.urls import path
from . import views
from .views import (PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView)

urlpatterns = [
    # path('',views.HomePage,name='HomePage'),

    path('',PostListView.as_view(),name='HomePage'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
    path('post/new/',PostCreateView.as_view(),name='post_create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post_update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post_delete'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
    path('MainPage/',views.MainPage,name='MainPage'),
    path('base/',views.Base,name='BasePage')
]

#<app>/<model>_<viewtype>.html  = DjangoApp/post_list.html


