def first():
    def try_to_change_values(some_list, num):
        for i_index, i_val in enumerate(some_list):
            some_list[i_index] += 10
        num += 10

    my_list = [1, 2, 3]
    number = 100

    try_to_change_values(my_list, number)
    print(my_list, number)

#hometask

def one():
    import random
    import copy

    def change_dict(dct):

        num = random.randint(1, 100)

        for i_key, i_value in dct.items():

            if isinstance(i_value, list):
                i_value.append(num)

            if isinstance(i_value, dict):
                i_value[num] = i_key

            if isinstance(i_value, set):
                i_value.add(num)

    nums_list = [1, 2, 3]
    some_dict = {1: 'text', 2: 'another text'}
    uniq_nums = {1, 2, 3}
    common_dict = {1: nums_list.copy(), 2: some_dict.copy(), 3: uniq_nums.copy(), 4: (10, 20, 30)}
    # change_dict(common_dict)
    # print(common_dict)
    common_dict_2 = copy.deepcopy(common_dict)  # Она будет особенно полезна в структурах, в которых множество вложенных переменных
    change_dict(common_dict_2)
    print(common_dict_2)
    print(nums_list, some_dict, uniq_nums)

def two():
    data = (1, 2, 3)
    print(f'Тип данных: {type(data)} ')
    
    if isinstance(data, list) or isinstance(data, dict) or isinstance(data, set):
        print('Изменяемый (mutable)')
    else:
        print('Неизменяемый (immutable)')

    print(f'ID объекта: {id(data)}')
    
two()