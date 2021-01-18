from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.urls import reverse
from .models import Blog, Info

# def base(request):
#     return render_to_response('base.html')

def blog(request):
	blog = Blog.objects.all()
	info = Info.objects.all()
	return render(request, 'base.html', {'blog' : blog, 'info' : info})

def addlike(request, pk):
	blog = get_object_or_404(Blog, id=request.POST.get('blog_id'))
	blog.like.add(request.user)
	return HttpResponseRedirect(reverse('like_blog', args=[str(pk)]))