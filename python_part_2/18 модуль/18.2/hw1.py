import re
text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'
result = re.match(r'wo', text)
print('Определить, начинается ли текст с шаблона wo: {}'.format(result))

print('='*40)
result = re.search(r'wo', text)
print('Найти первое упоминание шаблона wo в тексте: {}'.format(result))

print('='*40)
result = re.search(r'wo', text)
print(result.group(0))

print('='*40)
print(result.start())

print('='*40)
print(result.end())

print('='*40)
result = re.findall(r'wo', text)
print('Получить список из каждого упоминания шаблона wo в тексте: {}'.format(result))

print('='*40)
result = re.sub(r'wo', 'Замена', text)
print('Замена всех найденных шаблонов: {}'.format(result))