from django.urls import path, include
from .views import *
from django.conf import settings
from rest_framework import routers
from django.urls import path,include
from django.conf.urls.static import static

routers = routers.DefaultRouter()
routers.register('product', ProductViewSet)
routers.register('attribute', AttributeViewSet)




urlpatterns = [
    path('', include(routers.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

