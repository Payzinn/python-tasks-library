number_file = open('numbers.txt', 'r', encoding='utf-8')
numbers_list = []
for line in number_file:
    numbers_list.append(int(line))

number_file.close()

result = sum(numbers_list)
answer_file = open('answer.txt', 'w', encoding='utf-8')
answer_file.write(str(result))
answer_file.close()