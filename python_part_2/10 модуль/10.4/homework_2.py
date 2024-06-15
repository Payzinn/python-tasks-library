def counter_palindrome(words_list):
    counter = 0
    line_counter = 0
    try:
        for line in words_list:
            line_counter += 1
            if line == line[::-1]:
                counter += 1
            elif line.isdigit():
                raise TypeError
        
    except TypeError as exc:
        errors_file = open('errors.log', 'a', encoding='utf-8')
        errors_file.write(f'Произошла ошибка: {exc}, {type(exc)} в {line_counter}  строке' + '\n')
        errors_file.close()
        

    finally:
        result = ('Кол-во палиндромных слов: {}'.format(counter))
        return result
            
words_file = open('words.txt', 'r', encoding='utf-8')
content = words_file.read().split('\n')
words_file.close()
result = counter_palindrome(content)
print(result)