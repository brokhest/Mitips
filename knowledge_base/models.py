from django.db import models

# Create your models here.


class CarType(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class IntAttribute(Attribute):
    low_value = models.IntegerField()
    high_value = models.IntegerField()
    car_type = models.ForeignKey(CarType, related_name="int_attrs", on_delete=models.CASCADE)


class CharAttribute(Attribute):
    values = models.CharField(max_length=200)
    car_type = models.ForeignKey(CarType, related_name="char_attrs", on_delete=models.CASCADE)


class BoolAttribute(Attribute):
    value = models.CharField(max_length=10)
    car_type = models.ForeignKey(CarType, related_name="bool_attrs", on_delete=models.CASCADE)


class StIntAttribute(Attribute):
    low_value = models.IntegerField()
    high_value = models.IntegerField()


class StCharAttribute(Attribute):
    values = models.CharField(max_length=200)


class StBoolAttribute(Attribute):
    value = models.CharField(max_length=10)
