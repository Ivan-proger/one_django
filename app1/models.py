from django.db import models



class Blog(models.Model):
	name_blog = models.CharField('название', max_length=200)
	text_blog = models.TextField('текст поста')
	time = models.DateTimeField('дата')

	def __str__(self):
		return self.name_blog

	class Meta:
		verbose_name = 'пост'
		verbose_name_plural = 'посты'
