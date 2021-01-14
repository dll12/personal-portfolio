from django.shortcuts import render
from .models import Blog

def blog(request):
    blogs = Blog.objects.order_by('-dat')[:3]
    return render(request,'blog/blog.html',{'blogs':blogs})

