def first():
    students = {
    1: {
    'name': 'Bob',
    'surname': 'Vazovski',
    'age': 23,
    'interests': ['biology, swimming']
    },
    2: {
    'name': 'Rob',
    'surname': 'Stepanov',
    'age': 24,
    'interests': ['math', 'computer games', 'running']
    },
    3: {
    'name': 'Alexander',
    'surname': 'Krug',
    'age': 22,
    'interests': ['languages', 'health food']
    }
    }

    def interest_and_surname(students):
        interest_list = []
        counter = 0
        for i_interest in students:
            interest_list.extend(students[i_interest]['interests'])
            counter += len(students[i_interest]['surname'])
        return interest_list, counter

    id_and_age = []
    for i_age in students:
        id_and_age.append((i_age, students[i_age]['age']))

    main_function = interest_and_surname(students)
    print(main_function)
    print(id_and_age)

first()