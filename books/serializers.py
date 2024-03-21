from rest_framework import serializers
from .models import Books, Category


class CategorySerializer(serializers.Serializer):
    class Meta:
        models = Category
        fields = ['name']


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'title', 'author', 'description',
                  'front_thumbnail', 'back_thumbnail', 'category']
