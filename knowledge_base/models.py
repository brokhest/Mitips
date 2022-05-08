from django.db import models

# Create your models here.


class CarType(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class IntAtribute(models.Model):
    name = models.CharField(max_length=30)
    low_value = models.IntegerField()
    high_value = models.IntegerField()
    car_type = models.ForeignKey(CarType, related_name="int_atrs", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CharAtribute(models.Model):
    name = models.CharField(max_length=30)
    values = models.CharField(max_length=200)
    car_type = models.ForeignKey(CarType, related_name="char_atrs", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class BoolAtribute(models.Model):
    name = models.CharField(max_length=30)
    value = models.BooleanField()
    car_type = models.ForeignKey(CarType, related_name="bool_atrs", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
