# Generated by Django 3.1.5 on 2021-01-20 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20210115_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='like',
        ),
        migrations.AddField(
            model_name='blog',
            name='like',
            field=models.IntegerField(default='0'),
        ),
    ]