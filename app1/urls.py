from django.urls import path
from django.conf.urls import url
from .views import blog, addlike, blog_page

urlpatterns = [
	path(r'blog/like/<int:blog_id>', addlike, name='like_blog'),
	path(r'blog/', blog, name='blog'),
	path('blog/<int:blog_id>', blog_page),
]