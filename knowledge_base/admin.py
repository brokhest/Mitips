from django.contrib import admin
from .models import CarType, CharAttribute, IntAttribute, BoolAttribute, StCharAttribute, StIntAttribute, StBoolAttribute

# Register your models here.
admin.site.register(CarType)
admin.site.register(CharAttribute)
admin.site.register(IntAttribute)
admin.site.register(BoolAttribute)
admin.site.register(StIntAttribute)
admin.site.register(StCharAttribute)
admin.site.register(StBoolAttribute)
