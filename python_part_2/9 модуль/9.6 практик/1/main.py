numbers_file = open('numbers.txt', 'r')
numbers = []
for line in numbers_file:
    line_numbers = line.split()
    for number in line_numbers:
        numbers.append(int(number))
numbers_file.close()

total_sum = sum(numbers)

answer_file = open('answer.txt', 'w')
answer_file.write(str(total_sum))
answer_file.close()
