import os

file_path = os.path.join('numbers.txt')

numbers_file = open(file_path, 'r', encoding='utf-8')
nums = []

for line in numbers_file:
    nums.append(int(line))

numbers_file.close()
result = sum(nums)

answer_file = open('answer.txt', 'w')
answer_file.write(str(result))
answer_file.close()

