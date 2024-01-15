
with open('registrations.txt','r',encoding='utf-8') as reg_file:
    for i_line in reg_file:
        info = i_line.split()
        try:
            if len(info) != 3 or len(info) > 3:
                raise IndexError('{} Должно быть 3 поля'.format(info))
            
            if not info[0].isalpha():
                raise NameError('{} Имя должно содержать только буквы'.format(info))
            
            if '@' not in info[1] and '.' not in info[1]:
                raise SyntaxError('{} Поле email не содержит @ или точку'.format(info))
            
            if int(info[2]) > 99 or int(info[2]) < 10:
                raise ValueError('{} Возраст должен быть от 10 до 99 лет'.format(info))
            
            with open('registrations_good.log', 'a', encoding='utf-8') as log_file:
                for i_word in info:
                    log_file.write(str(i_word) + ' ')
                    if i_word.isdigit():
                        log_file.write('\n')        

        except IndexError as exc:
            print(exc)
            continue

        except NameError as exc:
            print(exc)
            continue

        except SyntaxError as exc:
            print(exc)
            continue

        except ValueError as exc:
            print(exc)
            continue
        
