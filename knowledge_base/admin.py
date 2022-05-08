from django.contrib import admin
from .models import CarType, CharAtribute, IntAtribute, BoolAtribute

# Register your models here.
admin.site.register(CarType)
admin.site.register(CharAtribute)
admin.site.register(IntAtribute)
admin.site.register(BoolAtribute)