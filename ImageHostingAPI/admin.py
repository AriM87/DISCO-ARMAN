from django.contrib import admin
from .models import CustomUser,Subscription,Image

admin.site.register(CustomUser)
admin.site.register(Subscription)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['user', 'image', 'thumbnail_200px', 'thumbnail_400px', 'created_at', 'is_link_linkable']
