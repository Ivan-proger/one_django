from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
	name_blog = models.CharField('название', max_length=200)
	text_blog = models.TextField('текст поста')
	time = models.DateTimeField('дата')
	like = models.IntegerField(default='0')

	def __str__(self):
		return self.name_blog

	class Meta:
		verbose_name = 'пост'
		verbose_name_plural = 'посты'


class Info(models.Model):
	name = models.CharField(default='SOME STRING', max_length=200)
	main_text = models.TextField("основной текст сообщения в правом садбаре")
	text = models.TextField("сообщение ниже главного текста кврсиавом")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "cooбщение"
		verbose_name_plural = "сообщения"	
