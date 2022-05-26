from django.shortcuts import render
from rest_framework.response import Response
from book import Book
from rest_framework import status, filters
from book import BookSerializer
from rest_framework import viewsets
from book import serializers, models
from rest_framework.settings import api_settings


class BookViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.BookSerializers
    queryset = models.Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    filters_backends = (filters.SearchFilter,)
    search_fields = ('title', 'genre', 'author',)

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.Book = None

    def list(self, request):
        a_viewset = [
            f'{self.Book.title}, {self.Book.genre}, {self.Book.author}, {self.Book.language} '
        ]
        return Response({'message': 'Book', 'a_viewset': a_viewset})

    def create(self, request):
        serializer = self.serializer_class(dat=request.data)
        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            return Response()
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

class BookFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.BookFeedItemSerializer
    queryset = models.BookFeedItem.objects.all()

    def perform_create(self, serializer):
        serializer.save(book=self.request.book)
