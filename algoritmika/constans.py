from collections import namedtuple

STATUS = {
    "1": "pending approval",
    "2": "approve",
    "3": "refuse",
}

Book = namedtuple('Book', ['id', 'name'])

book = []

books = [
    {
        "name": "Алексей",
        "id": 1
    }
]

note = [
    {
        "id": 1,
        "title": "First",
        "likes": 9,
        "tags": "a",
        "header": "Какак",
        "status": "pending approval",

    },
    {
        "id": 2,
        "title": "Second",
        "likes": 11,
        "tags": "и",
        "header": "ТаКак",
        "status": "approve",

    },
    {
        "id": 3,
        "title": "Second",
        "likes": 10,
        "tags": ["a", "n"],
        "header": "Татак",
        "status": "refuse",

    },
]

issue = [
    {
        "id": 1,
        "title": "Fssiue",
        "text": "Issiue Text",
        "executor": "Executor",
        "tags": "tags",
        "autor": "autor",
        "updated": "10 число до рождества христова",
        "created": "today",

    },
    {
        "id": 2,
        "title": "Kssiue",
        "text": "Issiue Text",
        "executor": "Executor",
        "tags": "tags",
        "autor": "autor",
        "updated": "10 число до рождества христова",
        "created": "today",

    },
    {
        "id": 3,
        "title": "Mssiue",
        "text": "Issiue Text",
        "executor": "Executor",
        "tags": "tags",
        "autor": "autor",
        "updated": "10 число до рождества христова",
        "created": "today",

    },
    {
        "id": 4,
        "title": "Assiue",
        "text": "Issiue Text",
        "executor": "Executor",
        "tags": "tags",
        "autor": "autor",
        "updated": "10 число до рождества христова",
        "created": "today",

    },
]
