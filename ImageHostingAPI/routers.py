from rest_framework import routers
from .views import ImageViewSet

router = routers.DefaultRouter()
router.register(r'uploadImage', ImageViewSet, basename='uploadImage')
