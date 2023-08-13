from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.conf import settings


class Subscription(models.Model):
    DEFAULT_PLANS = [
        ('basic', 'Basic'),
        ('premium', 'Premium'),
        ('enterprise', 'Enterprise'),
        ('arbitary', 'Arbitary'),
    ]
    plan = models.CharField(max_length=15, choices=DEFAULT_PLANS, default='basic')
    thumbnail_size = models.PositiveIntegerField(blank=True, null=True)
    origignal_file_link = models.BooleanField(default=False)
    link_expirable = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ('plan',)

    def __str__(self):
        return self.plan


class CustomUser(AbstractUser):
    plan = models.ForeignKey(
        Subscription, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/")

    # TODO: Make sure in next iteration to move this logic handeling to views.py
    def set_thumbnail_height_not_basic(self):
        return 400 if self.user.plan.plan != "basic" else 0

     # TODO: I do not think we actually need the following.
     # Once the Pillow is up and running and
     # user_plan handeling is embeded in views.py the following model needs to be updated.
    thumbnail_200px = ImageSpecField(source='image',
                                     processors=[ResizeToFill(height=200)],
                                     format='JPEG',
                                     options={'quality': 60})

    thumbnail_400px = ImageSpecField(source='image',
                                     processors=[ResizeToFill(
                                        height=set_thumbnail_height_not_basic)],
                                     format='JPEG',
                                     options={'quality': 60})

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    is_link_linkable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
