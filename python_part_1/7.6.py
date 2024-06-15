def first():
    names = ['Tom', 'Bob', 'Albert']
    ages = [20, 45, 70, 100]#zip выбрасывает последнее число
    people = list(zip(names,ages))
    people_1 = dict(zip(names,ages))
    #print(people)
    print(people_1)
    # for i in people:
    #     print(i)


first()