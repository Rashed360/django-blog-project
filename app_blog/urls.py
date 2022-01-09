from django.urls import path
from . import views

app_name = 'app_blog'

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('blog/', views.blog, name='blog'),
]
