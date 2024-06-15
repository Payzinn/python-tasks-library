import itertools

colors = ['красный', "синий", "зелёный", "жёлтый"]

for item in itertools.permutations(colors, 2):
    print(item)

print('='*40)

for item in itertools.combinations(colors, 2):
    print(item)

my_cycle = itertools.cycle(['раз', "два", "три"])
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))
