from django.contrib import admin
from .models import Post
from .models import Comment
from .models import Category
from .models import Book
from .models import Author
from .models import Genre

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)