from world import Birds, Food, Animals

print('*' * 25)
birds = Birds.import_from_file('birds.src')
[print(el) for el in birds]

print('*' * 25)
animals = Animals.import_from_file('animals_1.src')
[print(el) for el in animals]

print('*' * 25)
food = Food.import_from_file('food.src')
[print(el) for el in food]
