from django.db import models

# Create your models here.


class SoilValues(models.Model):
    soil_moisture = models.FloatField(null=False, blank=False)
    soil_temp     = models.FloatField(null=False, blank=False)
    soild_ph      = models.IntegerField(null=False, blank=False)
    stifler_id    = models.TextField(max_length=14, null=False, blank=False)
    taken_date    = models.DateTimeField(auto_now_add=True, verbose_name="taken datetime") 
