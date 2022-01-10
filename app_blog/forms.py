from django import forms
from django.forms import fields, widgets
from app_blog.models import Blog, Comment


class CommentForm(forms.ModelForm):
    comment = forms.CharField(label="", widget=forms.Textarea(attrs={'rows':'1',}))
    class Meta:
        model = Comment
        fields = ('comment',)
