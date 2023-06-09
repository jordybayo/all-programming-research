from django.conf import settings
from django.db import models

from django.core.serializers import serialize

import json
# Create your models here.

def upload_update_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)

class UpdateQuerySet(models.QuerySet):
    # def serializee(self):
    #     qs = self
    #     return serialize("json", qs, fields=('user', 'content', 'image'))

    def serialize(self):
        qs = self
        final_array = []
        for obj in qs:
            struct = json.loads(obj.serialize())
            final_array.append(struct)
        return json.dumps(final_array)

class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)

class Update(models.Model):
    #user        = models.ForeignKey(to=, on_delete=)
    content     = models.TextField(blank=True, null=True)
    image       = models.ImageField(upload_to='', blank=True, null=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = UpdateManager()

    def __str__(self): 
        return self.content or ""
    
    def serialize(self):
        json_data = serialize("json", [self], fields=("user", "content", "image"))
        struct = json.loads(json_data)
        print(struct)
        data = json.dumps(struct[0]['fields'])
        return data