sym_sum = 0
line_count = 0
with open('people.txt', 'r') as people_file:
    for i_line in people_file:
        try:
            length = len(i_line)
            line_count += 1
            
            if i_line.endswith('\n'):
                length -= 1
                
            if length < 3:
                raise ValueError('Длина {} строки меньше 3-х символов'.format(line_count))
                
            sym_sum += length
        except ValueError as exc:
            print(exc)
            continue

print('Найденная сумма символов: {}'.format(sym_sum))

