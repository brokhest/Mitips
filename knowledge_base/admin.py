from django.contrib import admin
from .models import CarType, CharAttribute, IntAttribute, BoolAttribute

# Register your models here.
admin.site.register(CarType)
admin.site.register(CharAttribute)
admin.site.register(IntAttribute)
admin.site.register(BoolAttribute)