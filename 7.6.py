def first():
    names = ['Tom', 'Bob', 'Albert']
    ages = [20, 45, 70, 100]#zip выбрасывает последнее число
    people = list(zip(names,ages))
    people_1 = dict(zip(names,ages))
    print(people)
    print(people_1)
    # for i in people:
    #     print(i)
    people_2 = {
        i_name: i_age + 10
        for i_name, i_age in zip(names,ages)
    }
    print(people_2)


first()