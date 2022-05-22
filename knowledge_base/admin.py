from django.contrib import admin
from .models import CarType, CharAttribute, FloatAttribute, BoolAttribute,\
    StCharAttribute, StFloatAttribute, StBoolAttribute, StInitAttribute

# Register your models here.
admin.site.register(CarType)
admin.site.register(CharAttribute)
admin.site.register(FloatAttribute)
admin.site.register(BoolAttribute)
admin.site.register(StFloatAttribute)
admin.site.register(StCharAttribute)
admin.site.register(StBoolAttribute)
admin.site.register(StInitAttribute)
