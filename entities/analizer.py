from rest_framework.utils import json

from knowledge_base.models import CarType
from .models import Entity
from knowledge_base.check import check_integrity


class Score(object):
    total = 0
    passed = 0
    name = ""


def analyze(entity):
    if not len(check_integrity()) == 0:
        return 2
    fit = []
    all_res = []
    for car_type in CarType.objects.all():
        score = Score()
        score.total = 0
        score.passed = 0
        score.name = car_type.name
        for float_atr in car_type.float_attrs.all():
            if entity.description.get(float_atr.name) is None:
                continue
            score.total += 1
            if float_atr.low_value <= float(entity.description.get(float_atr.name)) <= float_atr.high_value:
                score.passed += 1
        for char_atr in car_type.char_attrs.all():
            if entity.description.get(char_atr.name) is None:
                continue
            score.total += 1
            if char_atr.values.find(entity.description.get(char_atr.name)) >= 0:
                score.passed += 1
        for bool_atr in car_type.bool_attrs.all():
            if entity.description.get(bool_atr.name) is None:
                continue
            score.total += 1
            if bool_atr.value.find(entity.description.get(bool_atr.name)) >= 0:
                score.passed += 1
        response = {
            "name": car_type.name,
            "total": score.total,
            "passed": score.passed
        }
        # добавить - сравнение результатов: выбор класса и присвоение класса
        if score.total == 0:
            continue
        fit.append(response)
        all_res.append(score)
    if len(all_res) == 0:
        return 0
    classes = decide(all_res)
    if classes == 0:
        return 1
    # entity.car_type = CarType.objects.get(name=)
    fit = {
        "results": fit,
        "car type": classes
    }
    return fit


def decide(results):
    for res in results:
        res.score = res.passed/res.total
    num = -1
    classes = []
    for res in results:
        if res.score == 1:
            # max = res.score
            # total = res.total
            record = {
                "name": res.name
            }
            classes.append(record)
    if not len(classes) == 0:
        return classes
    else:
        return 0
