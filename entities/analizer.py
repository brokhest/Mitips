from knowledge_base.models import CarType
from .models import Entity


class Score(object):
    total = 0
    passed = 0
    name = ""


def analyze(entity):
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
    name = deside(all_res)
    if name == 0:
        return 1
    entity.car_type = CarType.objects.get(name=name)
    fit = {
        "results": fit,
        "car type": name
    }
    return fit


def deside(results):
    for res in results:
        res.score = res.passed/res.total
    max = 0
    num = -1
    total = 0
    for res in results:
        if res.score == 1 and res.total > total:
            max = res.score
            total = res.total
            num = results.index(res)

    if num >= 0:
        return results[num].name
    else:
        return 0
