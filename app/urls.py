from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DriverViewSet, CarViewSet, FineViewSet

router = DefaultRouter()
router.register(r'drivers', DriverViewSet, basename='driver')
router.register(r'cars', CarViewSet, basename='car')
router.register(r'fines', FineViewSet, basename='fine')

urlpatterns = [
    path('', include(router.urls)),
]