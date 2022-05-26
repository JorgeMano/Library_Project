from rest_framework.response import Response
from author import Author
from rest_framework import status, filters
from author import AuthorSerializer
from rest_framework import viewsets
from author import serializers, models
from rest_framework.settings import api_settings

class AuthorViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.AuthorSerializers
    queryset = models.Author.objects.all()
    filters_backends = (filters.SearchFilter,)
    search_fields = ('firstName', 'lastName', 'genre',)

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.Author = None

    def list(self, request):
        a_viewset = [
            f'{self.Author.firstName}, {self.Author.lastName}, {self.Author.genre}'
        ]
        return Response({'message': 'Author', 'a_viewset': a_viewset})

    def create(self, request):
        serializer = self.serializer_class(dat=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response()
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

class AuthorFeedViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.AuthorFeedItemSerializer
    queryset = models.AuthorFeedItem.objects.all()


    def perform_create(self, serializer):
        serializer.save(author=self.request.author)

