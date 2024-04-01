import re# regular expressions
text = 'AV - Analytics Vidhya AV'
result = re.match(r'AV', text)# поиск в начале строки по шаблону
print('Поиск в начале строки по шаблону {res}'.format(res = result))
print(result.group(0))
print(result.start())
print(result.end())

result = re.match(r'Analytics', text)
print(result)

print('='* 40)
result = re.search(r'Analytics', text)# поиск в строке по шаблону
print("Поиск в строке по шаблону: {}".format(result))
print(result.group(0))

print('='* 40)
result = re.findall(r'AV', text)# поиск совпадения по шаблону
print("Поиск в строке по шаблону: {}".format(result))

print('='* 40)
text_2 = 'AV is largest Analytics community of India. India!'
result = re.sub(r'India', 'the World', text_2)#Замена всех найденных шаблонов
print('Замена всех найденных шаблонов: {}'.format(result))
print('='* 40)

pattern = re.compile('AV')
result = pattern.findall(text)
print(result)
result2 = pattern.findall(text_2)
print(result2)