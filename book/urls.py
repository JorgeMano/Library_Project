from django.urls import path, include
from rest_framework.routers import DefaultRouter
from book import views

router = DefaultRouter()
router.register('book', views.BookViewSet)

urlpattens = [
    path('', include(router.urls)),
]