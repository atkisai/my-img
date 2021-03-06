# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-11 16:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название альбома')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Ссылка для альбома')),
                ('img', models.ImageField(upload_to='images', verbose_name='Изображение альбома')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название фотографии')),
                ('img', models.ImageField(upload_to='images', verbose_name='Фото')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Album', verbose_name='Альбом')),
            ],
        ),
    ]
