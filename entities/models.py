from django.db import models
from knowledge_base.models import CarType


# Create your models here.
class Entity(models.Model):
    description = models.JSONField()
    name = models.CharField(max_length=20, default="")
    car_type = models.ForeignKey(CarType, related_name="cars", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
