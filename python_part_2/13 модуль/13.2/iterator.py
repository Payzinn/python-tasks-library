items = [10, 20, 30]
iterator = iter(items)
print(iterator)

for i in iterator:
    print(i)

iterator = iter(items)

print(iterator.__next__())
print(next(iterator))
print(next(iterator))