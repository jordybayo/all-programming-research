from django.db import models
from django.conf import settings

def upload_status_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)

# Create your models here.
class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_status_image)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)[:50]
    
    class Meta:
        verbose_name = 'Status post'
        verbose_name_plural = 'Status posts'

    
    