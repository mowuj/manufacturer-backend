from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views
router = DefaultRouter()

router.register('products', views.ProductViewset)
router.register('category', views.CategoryViewset)


urlpatterns = [
    path('', include(router.urls)),
]
