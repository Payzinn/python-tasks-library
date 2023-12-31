def first():
    # Задаём исходные данные
    target = "a"
    text = "mhtirogla"

    # Инициализируем переменную для проверки успеха поиска
    success = False

    # Запускаем цикл по каждому символу в тексте
    for letter in text:
        # Сравниваем текущую букву с искомой
        if letter == target:
            # Если совпадение найдено, обновляем статус и прерываем цикл
            success = True
            break

    # Выводим результат поиска
    if success:
        print("Буква была найдена в строке")
    else:
        print("Буквы в строке нет")

def second():
    text = 'довод'
    reversed_text = ''

    # Проходим по всей строке
    for letter in text:
        # Каждый символ строки добавляем В НАЧАЛО новой строки
        reversed_text = letter + reversed_text

    # В итоге в reversed_text мы получим перевёрнутую строку.
    # Если строки равны, слово является палиндромом
    if text == reversed_text:
        print('Это палиндром!')
    else:
        print('Не палиндром!')

def third():
    # Возьмём тот же текст
    text = 'довод'
    # Нам понадобится узнать его длину
    text_length = len(text)
    # И вспомогательный флаг
    success = True


    # За одну итерацию мы будем проверять два символа (с начала и с конца),
    # поэтому итераций можно сделать в два раза меньше (text_length // 2):
    for i in range(text_length // 2):
        # На каждой итерации сравниваем два символа:
        # символ с начала text[i] с символом с конца text[-i - 1]
        if text[i] != text[-i - 1]:
            # Если хотя бы одна пара символов не совпадёт, то меняем флаг и завершаем цикл
            success = False
            break

    # Если все символы совпадают, то строка является палиндромом, иначе — нет
    if success:
        print('Это палиндром!')
    else:
        print('Не палиндром!')


def myVariant():
    text = 'шалаш'
    if text == text[::-1]:
        print('палиндром')
    else:
        print('не палиндром')