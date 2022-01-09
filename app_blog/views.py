from django.shortcuts import render

def blogs(request):
    context={}
    return render(request, 'app_blog/blogs.html', context)

def blog(request):
    context={}
    return render(request, 'app_blog/blog.html', context)