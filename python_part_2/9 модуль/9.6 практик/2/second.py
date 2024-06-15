zen_file = open('zen.txt', 'r', encoding='utf-8')
content = zen_file.read()   
result = (content.split('.'))
for line in reversed(result):
    print(line + '.')