from django.urls import path
from .views import blog

urlpatterns = [
	path(r'', blog, name='blog'),
]