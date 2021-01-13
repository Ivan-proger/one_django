from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Blog, Info

def blog(request):
	blog = Blog.objects.all()
	info = Info.objects.all()
	return render(request, 'home.html', {'blog' : blog, 'info' : info})


