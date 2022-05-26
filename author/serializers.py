from rest_framework import serializers
from author import models.Author

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model: models.Author
        fields = ('id', 'firstName', 'lastName', 'genre')

    def create(self, validated_data):
        author = models.Author.object.create_author(
            firstName=validated_data['firstName'],
            lastName=validated_data['lastName'],
            genre=validated_data['genre']
        )
        return author

class AuthorFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuthorFeedItem
        fields = ('id', 'firstName', 'lastName', 'status_text', 'created_on')
