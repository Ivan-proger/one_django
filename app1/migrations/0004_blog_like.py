# Generated by Django 3.1.5 on 2021-01-14 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_info_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='like',
            field=models.IntegerField(default='0'),
        ),
    ]