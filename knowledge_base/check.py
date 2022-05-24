from .models import StCharAttribute, StBoolAttribute, StFloatAttribute,\
    FloatAttribute, CharAttribute, BoolAttribute, CarType, StInitAttribute, StAttribute, Attribute


def check_integrity():
    data = []
    for attr in StAttribute.objects.all():
        if len(Attribute.objects.filter(name=attr.name)) == 0:
            record = {
                "attribute": attr.name,
                "reason": "no classes"
            }
            data.append(record)
    for attr in StInitAttribute.objects.all():
        record = {
            "attribute": attr.name
        }
        data.append(record)
    for attr in StBoolAttribute.objects.all():
        if attr.value == ", " or attr.value == "":
            record = {
                "attribute": attr.name
            }
            data.append(record)
    for attr in StCharAttribute.objects.all():
        if attr.values == "," or attr.values == "":
            record = {
                "attribute": attr.name
            }
            data.append(record)
    for attr in StFloatAttribute.objects.all():
        if attr.low_value == attr.high_value == 0:
            record = {
                "attribute": attr.name
            }
            data.append(record)
    for car in CarType.objects.all():
        if not (car.float_attrs.all().exists() + car.char_attrs.all().exists() + car.bool_attrs.all().exists()):
            record = {
                "car type": car.name
            }
            data.append(record)
        else:
            for attr in car.float_attrs.all():
                if attr.low_value == attr.high_value == 0:
                    record = {
                        "car type": car.name,
                        "attribute": attr.name
                    }
                    data.append(record)
            for attr in car.bool_attrs.all():
                if attr.value == ", " or attr.value == "":
                    record = {
                        "car type": car.name,
                        "attribute": attr.name
                    }
                    data.append(record)
            for attr in car.char_attrs.all():
                if attr.values == ", " or attr.values == "":
                    record = {
                        "car type": car.name,
                        "attribute": attr.name
                    }
                    data.append(record)
    return data


def check(st_attribute, attribute, type):
    if type == "float":
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
            print(st_attribute.value.find(value))
            if st_attribute.value.find(value) == -1:
                return 0
        return 1


def change_type_car(type, new_type, name, new_name):
    if type == "float":
        if new_type == "char":
            for attr in FloatAttribute.objects.filter(name=name):
                car = attr.car_type
                attr.delete()
                car_attribute = CharAttribute(name=new_name, values="", car_type=car)
                car_attribute.save()
        elif new_type == "bool":
            for attr in FloatAttribute.objects.filter(name=name):
                car = attr.car_type
                attr.delete()
                car_attribute = BoolAttribute(name=new_name, car_type=car)
                car_attribute.save()
    elif type == "char":
        if new_type == "float":
            for attr in CharAttribute.objects.filter(name=name):
                car = attr.car_type
                attr.delete()
                car_attribute = FloatAttribute(name=new_name, low_value=0, high_value=0, car_type=car)
                car_attribute.save()
        elif new_type == "bool":
            for attr in CharAttribute.objects.filter(name=name):
                car = attr.car_type
                attr.delete()
                car_attribute = BoolAttribute(name=new_name, value="", car_type=car)
                car_attribute.save()
    elif type == "bool":
        if new_type == "float":
            for attr in BoolAttribute.objects.filter(name=name):
                car = attr.car_type
                attr.delete()
                car_attribute = FloatAttribute(name=new_name, low_value=0, high_value=0, car_type=car)
                car_attribute.save()
        elif new_type == "char":
            for attr in BoolAttribute.objects.filter(name=name):
                car = attr.car_type
                attr.delete()
                car_attribute = CharAttribute(name=new_name, values="", car_type=car)
                car_attribute.save()
    return


def change_type(st_attribute, request):
    name = st_attribute.name
    st_attribute.delete()
    if request.data.get("new type") == "float":
        attribute = StFloatAttribute(name=request.data.get("name"), low_value=float(request.data.get("low value")),
                                     high_value=float(request.data.get("high value")))
    elif request.data.get("new type") == "char":
        attribute = StCharAttribute(name=request.data.get("name"), values=request.data.get("values") + ",")
    elif request.data.get("new type") == "bool":
        attribute = StBoolAttribute(name=request.data.get("name"))
    attribute.save()
    change_type_car(request.data.get("attr type"), request.data.get("new type"), name, attribute.name)
    return


def change_name(st_attribute, type, new_name):
    if type == "float":
        for attribute in FloatAttribute.objects.filter(name=st_attribute.name):
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


def change_float(st_attribute, low_value, high_value):
    for attribute in FloatAttribute.objects.filter(name=st_attribute.name):
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


def delete_all(st_attribute):
        for attr in Attribute.objects.filter(name=st_attribute.name):
            attr.delete()
        return

