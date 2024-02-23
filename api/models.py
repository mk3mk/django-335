from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)
    posts = models.ManyToManyField('Post', related_name='categories', blank=True)

    class Meta:
        verbose_name_plural = 'categories'


class Book(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    author = models.ForeignKey('Author', related_name='books', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', related_name='books', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'books'


class Author(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        verbose_name_plural = 'authors'


class Genre(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        verbose_name_plural = 'genres'
