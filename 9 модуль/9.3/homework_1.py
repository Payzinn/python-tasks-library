import os
first_path = os.path.join('task', 'group_1.txt')
second_path = os.path.join('task','additional info', 'group_2.txt')
file_1 = open(first_path, 'r', encoding='utf-8')
file_2 = open(second_path, 'r', encoding='utf-8')

summa = 0
diff = 0
print('group_1.txt')
for i_line in file_1:
    info = i_line.split()
    summa += int(info[2])
    diff -= int(info[2])
    
print(' Сумма очков: {}'.format(summa))
print(' Разность очков: {}'.format(diff))
file_1.close()

compose = 1

print('\ngroup_2.txt')
for i_line in file_2:
    info = i_line.split()
    compose *= int(info[2])
print('  Произведение: {}'.format(compose))
file_2.close()