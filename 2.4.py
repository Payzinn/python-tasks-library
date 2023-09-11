scores=[5,2,4]
print(f'Начальный список игроков: {scores}')
first=len(scores)
print('длина списка:', first)
scores[1]+=first
print(f'Увеличение очков второго игрока: {scores}')
ask=int(input('\nСколько очков добавить следующему игроку: '))
scores.append(ask)
print(f'\nСписок с новым игроком: {scores}')
second=len(scores)
scores[2]+=second
print(f'\nТеперь добавляем третьему игроку очки \nСписок: {scores}')

