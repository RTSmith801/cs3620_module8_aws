from rest_framework import serializers
from .models import Author, Book, Loan

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_date', 'author', 'author_name']

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value


class LoanSerializer(serializers.ModelSerializer):
    borrower_name = serializers.ReadOnlyField(source='borrower.username')
    book_title = serializers.ReadOnlyField(source='book.title')

    class Meta:
        model = Loan
        fields = ['id', 'book', 'book_title', 'borrower_name', 'loan_date', 'returned']
