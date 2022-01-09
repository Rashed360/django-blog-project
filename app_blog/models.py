from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_author')
    title = models.CharField(max_length=264, verbose_name='Insert Title')
    slug = models.SlugField(max_length=264, unique=True)
    content = models.TextField(verbose_name='Blog Content')
    image = models.ImageField(upload_to='blogs', verbose_name='Image')
    published = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField(verbose_name='Blog Comment', default='')
    commented = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment

class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_like')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')

