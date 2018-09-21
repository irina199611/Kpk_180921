from world import Animals, Food, Birds

animals_source = open('animals.src', 'r', encoding='utf-8').readlines()
animals_source = list(map(lambda x: x.replace('\n', '').split(', '), animals_source))


students_schema = animals_source.pop(0)


students_source_as_dict = list(map(lambda x: dict(zip(students_schema, x)), animals_source))


