from rest_framework import serializers
from book import models.Book, models.BookItem

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model: models.Book
        fields = ('id', 'title', 'genre', 'author')

    def create(self, validated_data):
        book = models.Book.object.create_book(
            title=validated_data['title'],
            genre=validated_data['genre'],
            author=validated_data['author']
        )
        return book

class BookFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BookFeedItem
        fields = ('id', 'book', 'status_text', 'created_on')
