import random

def first():
    scores = [random.randint(10,110) for _ in range (5)]
    print("Изначальный список: ",scores)
    for i_player,i_score in enumerate(scores):
        print(i_player, i_score)

def second():
    sym = ["a",'b','c']
    gen = enumerate(sym)
    print(gen)

#выводит лениво, тоесть только тогда когда запросишь

#Home task

def one():
    def get_index(word, symbol):
        return [str(index) for index, letter in enumerate(word) if letter == symbol]
    text = input('Строка: ')
    print('Ответ', " ".join(get_index(text, "~")))


def two():
    def get_random_letter(n):
        return random.choices([chr(i) for i in range(ord("а"), ord("я"))], k=n)

    first_letters = get_random_letter(10)
    second_letters = get_random_letter(10)
    print(first_letters)
    print(second_letters)

    first_dictionary = dict(enumerate(first_letters))
    second_dictionary = dict(enumerate(second_letters))
    print(first_dictionary)
    print(second_dictionary)

def twoalt():
    first_list = ['й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к']
    second_list = ['д', 'а', 'а', 'в', 'т', 'ж', 'р', 'б', 'й', 'р']
    print('Первый список: {}\nВторой список:{}'.format(first_list,second_list))
    first_dict = dict(enumerate(first_list))
    second_dict = dict(enumerate(second_list))
    print('{}\n{}'.format(first_dict,second_dict))

def three():
    
    def even(word):
        result = []
        if isinstance(word,dict):
            word = word.values()
        for index, letter in enumerate(word):
            if index %2 == 0:
                result.append(letter)
        return result
    
    print(even('О Дивный Новый мир!'))
    print(even([100, 200, 300, 'буква', 0, 2, 'а']))
    print(even({0: 'е', 1: 'о', 2: 'ч', 3: 'ы', 4: 'в', 5: 'н', 6: 'д', 7: 'а', 8: 'ш', 9: 'ц'}))

