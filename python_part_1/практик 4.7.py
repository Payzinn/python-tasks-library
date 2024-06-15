

def first():
    vowells_list = ['а','о','у','ы','э','е','ё','и','ю','я','А','О','Ы','Э','Е','Ё','Ю','Я','И']
    text = input('Введите текст: ')
    vowells =[]
    for i in text:
        if i in vowells_list:
            vowells.append(i)

    print(text)
    print(vowells)
    print(f'длина списка: {len(vowells)}')

def second():   
    N = int(input('Введите длину списка: '))
    result=[1 if i % 2 == 0 or i == 0 else i % 5 for i in range(0,N)]
    print(result)

def third():
    import random as r
    first_team = [round(r.uniform(5,10),2) for _ in range(20)]
    second_team = [round(r.uniform(5,10),2) for _ in range(20)]
    third_team=[]
    for i in range(20):
        if first_team[i]>second_team[i]:
            third_team.append(first_team[i])
        else:
            third_team.append(second_team[i])
    print(f'первая: {first_team}')
    print(f'вторая: {second_team}')
    print(f'победители: {third_team}')

def fourth():
    alphabet = 'abcdefg'
    print(f'1: {alphabet}')
    print(f'2: {alphabet[::-1]}')
    print(f'3: {alphabet[0::2]}')
    print(f'4: {alphabet[1::2]}')
    print(f'5: {alphabet[:1]}')
    print(f'6: {alphabet[:-2:-1]}')
    print(f'7: {alphabet[3:4]}')
    print(f'8: {alphabet[-3:]}')
    print(f'9: {alphabet[3:5]}')
    print(f'10: {alphabet[4:2:-1]}')

def fivth():

    text = input('Введите строку: ')
    x = text.index('h')
    y = text.rindex('h')
    print(f"Развёрнутая последовательность между первым и последним h: {text[y-1:x:-1]}")

fivth()

def sixth():
    num_list = [[i+j*4 for j in range(4)] for i in range(1, 5)]
    print(num_list)

def seventh():

    nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
    output = [digit for each_list in nice_list for each_list_2 in each_list for digit in each_list_2 ]
    print(output)

def eight():
    
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    text = input('Введите сообщение: ').lower()
    step = int(input('Введите сдвиг: '))
    newlist = list(text)
    for i in newlist:
        if i == ' ':
            print(' ', end='')
            continue
        if i not in alphabet:
            continue
        x = alphabet.index(i)
        if x + step >= len(alphabet):
            x = x - len(alphabet)
        print(alphabet[x+step], end='')

