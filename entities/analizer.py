from knowledge_base.models import CarType
from .models import Entity


def analyze(entity):
    fit = []
    for car_type in CarType.objects.all():
        counter = 0
        attributes = 0
        for float_atr in car_type.float_attrs.all():
            attributes += 1
            if float_atr.low_value <= float(entity.get(float_atr.name)) <= float_atr.high_value:
                counter += 1
        for char_atr in car_type.char_attrs.all():
            attributes += 1
            if char_atr.values.find(entity.get(char_atr.name)) >=0:
                counter += 1
        for bool_atr in car_type.bool_attrs.all():
            attributes += 1
            if bool_atr.value.find(entity.get(bool_atr.name)) >= 0:
                counter += 1
        response = {
            "name": car_type.name,
            "total": attributes,
            "passed": counter
        }
        fit.append(response)
    return fit