from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, CategoryViewSet, TagViewSet, ObtainAuthToken

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', ObtainAuthToken.as_view(), name='api-token-auth'),
]