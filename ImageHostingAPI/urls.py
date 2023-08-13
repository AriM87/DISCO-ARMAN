from django.urls import path, include
from .views import ImageViewSet, ImageUploadView
from .routers import router

urlpatterns = [
    path('imageApi/', include(router.urls)),
    path('upload/', ImageUploadView.as_view(), name='upload'),
]
