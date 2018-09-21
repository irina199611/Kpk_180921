class Animals:
    def __init__(self, animals_name, country,):
        self.animals_name = animals_name
        self.country = country

    def __str__(self):
            return f'животное:{self.animals_name} {self.country}.'

    @classmethod
    def import_from_file(cls, world):
        items_source = open(world, 'r', encoding='utf-8').readlines()
        items_source = list(map(lambda x: x.replace('\n', '').split(', '), items_source))
        items_schema = items_source.pop(0)
        items_source_as_dict = list(map(lambda x: dict(zip(items_schema, x)), items_source))
        items = []
        for item_dict in items_source_as_dict:
            _item = cls(**item_dict)
            items.append(_item)
        return items


class Birds(Animals):
    def __init__(self, fly, something):
        self.fly = fly
        self.something = something

    def __str__(self):
            return f'птицы:{self.fly} {self.something}'


class Food(Animals):
    def __init__(self, food_name, country):
        self.food_name = food_name
        self.country = country

    def __str__(self):
            return f'Еда:{self.food_name} {self.country}'