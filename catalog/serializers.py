from rest_framework import serializers
from .models import Genre, Author, Book, BookInstance, Language, User

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = (
            'first_name',
            'last_name',
            'date_of_birth',
            'date_of_death'
        )

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'title',
            'author',
            'summary',
            'isbn',
            'genre',
            'language'
        )

class BookInstanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookInstance
        fields = (
            'book',
            'imprint',
            'due_back',
            'borrower'
        )

class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = (
            'name'
        )