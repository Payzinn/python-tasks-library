try:
    BRUCE_WILLIS = 42
    input_data = input('Введите строку: ')
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')

except IndexError as exc:
    print(type(exc),'- выход за границы списка')
except ValueError as exc:
    print(type(exc), '- невозможно преобразовать в число')
except Exception as exc:
    print(type(exc), '- поймано исключение')