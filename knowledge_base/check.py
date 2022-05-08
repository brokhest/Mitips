from .models import StCharAttribute, StBoolAttribute, StIntAttribute,\
    IntAttribute, CharAttribute, BoolAttribute, CarType


def check(st_attribute, attribute, type):
    if type == "int":
        return 1 if (st_attribute.low_value <= attribute.low_value <= st_attribute.high_value) and \
                    (st_attribute.low_value <= attribute.high_value <= st_attribute.high_value) else 0
    elif type == "char":
        values = attribute.values.split(", ")
        for value in values:
            value += ","
            if st_attribute.values.find(value) == -1:
                return 0
        return 1
    elif type == "bool":
        values = attribute.value.split(", ")
        for value in values:
            value += ","
            if st_attribute.value.find(value) == -1:
                return 0
        return 1


def change_name(st_attribute, type, new_name):
    if type == "int":
        for attribute in IntAttribute.objects.filter(name=st_attribute.name):
            attribute.name = new_name
            attribute.save()
    elif type == "char":
        for attribute in CharAttribute.objects.filter(name=st_attribute.name):
            attribute.name = new_name
            attribute.save()
    elif type == "bool":
        for attribute in BoolAttribute.objects.filter(name=st_attribute.name):
            attribute.name = new_name
            attribute.save()


def change_int(st_attribute, low_value, high_value):
    for attribute in IntAttribute.objects.filter(name=st_attribute.name):
        if attribute.low_value < low_value:
            attribute.low_value = low_value
        if attribute.high_value > high_value:
            attribute.high_value = high_value
        attribute.save()


def change_char(st_attribute, new_values):
    for attribute in CharAttribute.objects.filter(name=st_attribute.name):
        values = attribute.values.split(", ")
        for value in values:
            value += ","
            if new_values.find(value) == -1:
                attribute.values = attribute.values.replace(value, "")
        attribute.save()


def change_bool(st_attribute, new_value):
    for attribute in BoolAttribute.objects.filter(name=st_attribute.name):
        value = attribute.value.split(", ")
        for val in value:
            val += ","
            if new_value.find(val) == -1:
                attribute.value = attribute.value.replace(val, "")
        attribute.save()


