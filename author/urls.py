from django.urls import path, include
from rest_framework.routers import DefaultRouter
from author import views

router = DefaultRouter()
router.register('author', views.AuthorViewSet)

urlpattens = [
    path('', include(router.urls)),
]