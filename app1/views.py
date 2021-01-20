from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.urls import reverse
from .models import Blog, Info


def blog_page(request, blog_id):
    context = {
        'blog': Blog.objects.get(id=blog_id)
    }
    return render(request, "Blog_detail.html", context)

def blog(request):
	blog = Blog.objects.all()
	info = Info.objects.all()
	return render(request, 'base.html', {'blog' : blog, 'info' : info})

def addlike(request, blog_id):
   blog = get_object_or_404(Blog, id=blog_id)  # возвращает id статьи или 404.
   blog.like += 1 # Прибавляет единицу к article_likes
   blog.save() # сохраняет
   return HttpResponseRedirect('/blog')

