import operator


def sorted_entities(list_of_entity: list, key: str, parameter='asc'):
    is_asc = True
    if parameter == 'desc':
        is_asc = False
    list_of_entity.sort(key=operator.itemgetter(key), reverse=is_asc)
    return list_of_entity


def get_params_filter(key: str, params: dict):
    value = params[key]
    filter_func, value = value.split(':')
    if not (filter_func and value):
        raise ValueError()
    return filter_func, {'key': key, 'value': value.strip()}


def like(list_of_entity: list, key: str, value):
    tmp = []
    for entity in list_of_entity:
        result = entity[key].find(value)
        if result != -1:
            tmp.append(entity)
    return tmp


def eq(list_of_entity: list, key: str, value):
    tmp = []
    for entity in list_of_entity:
        if str(entity[key]) == str(value):
            tmp.append(entity)
    return tmp


def gte(list_of_entity: list, key: str, value):
    tmp = []
    for entity in list_of_entity:
        if entity[key] >= int(value):
            tmp.append(entity)
    return tmp


def gt(list_of_entity: list, key: str, value):
    tmp = []
    for entity in list_of_entity:
        if entity[key] >= int(value):
            tmp.append(entity)
    return tmp


def lt(list_of_entity: list, key: str, value):
    tmp = []
    for entity in list_of_entity:
        if entity[key] < int(value):
            tmp.append(entity)
    return tmp


def lte(list_of_entity: list, key: str, value):
    tmp = []
    for entity in list_of_entity:
        if entity[key] <= int(value):
            tmp.append(entity)
    return tmp


def occurrence_check(list_of_entity: list, key: str, value):
    tmp = []
    value = value.split(',')
    if not value:
        raise ValueError()
    for entity in list_of_entity:
        tags = entity[key]
        if any(map(lambda x: x in list(tags), value)):
            tmp.append(entity)
    return tmp


ORM_FALCON = {
    'like': like,
    'eq': eq,
    'gte': gte,
    'gt': gt,
    'lt': lt,
    'lte': lte,
    'in': occurrence_check,
}