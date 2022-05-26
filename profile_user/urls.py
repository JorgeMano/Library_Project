from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profile_user import views

router = DefaultRouter()
router.register('user', views.UsersViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view)
]