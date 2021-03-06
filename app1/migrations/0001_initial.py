# Generated by Django 3.1.2 on 2020-12-09 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_blog', models.CharField(max_length=200, verbose_name='название')),
                ('text_blog', models.TextField(verbose_name='текст поста')),
                ('time', models.DateTimeField(verbose_name='дата')),
            ],
            options={
                'verbose_name': 'пост',
                'verbose_name_plural': 'посты',
            },
        ),
    ]
