from django.urls import path, include
from category.api.views import *
from django.conf import settings
from rest_framework import routers
from django.conf.urls.static import static


routers = routers.DefaultRouter()
routers.register('category', CategoryViewSet)
routers.register('subcategory', SubCategoryViewSet)


urlpatterns = [
    path('', include(routers.urls)),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

