from django.urls import path
from app_blog  import views

app_name = 'app_blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blogs'),
    path('create/', views.CreateBlog.as_view(), name='create'),
    path('update/<pk>/', views.UpdateBlog.as_view(), name='update'),
    path('manage/', views.MyBlog.as_view(), name='manage'),
    path('delete/<pk>/', views.delete_blog, name='delete'),
    path('blog/<slug:slug>/', views.single_blog, name='blog'),
    path('like/<pk>/', views.like_blog, name='like'),
    path('dislike/<pk>/', views.dislike_blog, name='dislike'),
]