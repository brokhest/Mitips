from django.db import models


# Create your models here.


class CarType(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class StAttribute(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class FloatAttribute(Attribute):
    low_value = models.FloatField(null=True)
    high_value = models.FloatField(null=True)
    car_type = models.ForeignKey(CarType, related_name="float_attrs", on_delete=models.CASCADE)


class CharAttribute(Attribute):
    values = models.CharField(max_length=200, null=True)
    car_type = models.ForeignKey(CarType, related_name="char_attrs", on_delete=models.CASCADE)


class BoolAttribute(Attribute):
    value = models.CharField(max_length=10, null=True)
    car_type = models.ForeignKey(CarType, related_name="bool_attrs", on_delete=models.CASCADE)


class StFloatAttribute(StAttribute):
    low_value = models.FloatField(null=True)
    high_value = models.FloatField(null=True)


class StCharAttribute(StAttribute):
    values = models.CharField(max_length=200, null=True)


class StBoolAttribute(StAttribute):
    value = models.CharField(max_length=10, null=True, default="yes, no,")


class StInitAttribute(StAttribute):
    class Meta:
        verbose_name = u'Признак'
        verbose_name_plural = u'Признаки'
