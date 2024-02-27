from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Category
from .models import Book, Author, Genre


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'owner', 'posts']


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner', 'comments', 'categories', 'poster']


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'comments', 'categories']


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post']


class BookSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')
    genre = serializers.ReadOnlyField(source='genre.title')

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'cover']


class AuthorSerializer(serializers.ModelSerializer):
    # name = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Author
        fields = ['id', 'name']


class GenreSerializer(serializers.ModelSerializer):
    # title = serializers.ReadOnlyField(source='genre.title')
    # description = serializers.ReadOnlyField(source='genre.description')

    class Meta:
        model = Genre
        fields = ['id', 'title', 'description']