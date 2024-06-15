file_to_write = open('t', 'w', encoding='utf-8')
try:
    text_input = input('Введите текст: ')
    file_to_write.write(text_input)

except (FileNotFoundError, PermissionError) as exc:
    print(type(type),("Ошибка создания файла"))
except ValueError as exc:
    print(type(exc), '- Нельзя преобразовать данные в целое.')
except Exception as exc:
    print(type(exc), ('Поймано исключение.'))
else:
    print('Программа выполнилась без ошибок.')

finally:
    file_to_write.close()
    print(file_to_write.closed)