def first():
    def ask_user(question, 
                 complaint = "Неверный ввод. Введите да или нет", 
                 retries = 4):
        while True:
            answer = input(question).lower()
            if answer == 'да':
                return 1
            if answer == 'нет':
                return 0
            retries -= 1
            if retries == 0:
                print('Кол-во попыток истекло.')
                break
            print(complaint)
            print('Отсалось попыток: {}'.format(retries))
    
    ask_user("Вы действительно хотите выйти?")
    ask_user("Удалить файл?", "Так удалить или нет?")
    ask_user("Записать файл?", retries = 2)



def second():
    def ask_user(question, 
                 complaint = 'Неверно. Введите да или нет', 
                 attempt = 4):
        while True:
            answer = input(question)

            if answer == 'да':
                return 1
            
            if answer == "нет":
                return 0
            attempt -= 1

            if attempt == 0:
                print('Кол-во попыток истекло.')
                break

            print(complaint)
            print('Осталось попыток: {}'.format(attempt))
    
    ask_user("Пойти в колледж?")
    ask_user('Играть в клеш рояль?', "Так игать или нет?")
    ask_user('Пойти в качалку?', attempt = 2)


def third():
    def add_num(num, lst = None):
        lst = lst or []
        lst.append(num)
        print(lst) 
    
    add_num("a")

#third()

def alt_third():
    def add_num(num, nums=None):
        nums = nums or []
        # хитрая конструкция, которая позволит упростить ввод:
        # if not nums:
        #    nums = []
        # Первый вариант будет выбран, если nums не равен None, иначе будет создан и записан пустой список
        nums.append(num)
        print(nums)



def fourth():
    def create_dict(data, template = None):
        if isinstance(data, dict):
            return data

        if isinstance(data, int) or isinstance(data, float) or isinstance(data, str):
            template = template or dict()
            template[data] = data
            return template
        else:
            return None

    
    def data_preparation(old_list):
        new_list = []
        for i_element in old_list:
            new_elem = create_dict(i_element)
            if new_elem:
                new_list.append(create_dict(i_element))

        return new_list

    

    data = ["sad", {"sds": 23}, {43}, [12, 42, 1], 2323]
    data = data_preparation(data)
    print(data)

fourth()