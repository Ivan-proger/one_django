from django.urls import path
from django.conf.urls import url
from .views import blog, addlike

urlpatterns = [
	path(r'blog/like/<int:pk>', addlike, name='like_blog'),
	url(r'blog/', blog, name='blog'),
]