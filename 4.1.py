def first():
    nums = int(input('Количество чисел: '))
    digits = []
    for _ in range(nums):
        ask = int(input('Число: '))
        digits.append(ask)
    reverse_list=[]
    for i in range(len(digits)-2,-1,-1):
        reverse_list.append(digits[i])
    print(digits)
    print(reverse_list)

#e
def second():
    def is_palindrome(num_list):
        reversed_list = []

        for i in range(len(num_list)-1, -1, -1):
            reversed_list.append(num_list[i])
        if num_list == reversed_list:
            return True
        else:
            return False
        
    nums = int(input('Количество чисел: '))
    digits = [1,2,3,4,3,2]
    for _ in range(nums):
         ask = int(input('Число: '))
         digits.append(ask)

    new_nums = []
    answer = []

    for i in range(0, len(digits)):
        for j in range(i, len(digits)):
            new_nums.append(digits[j])
        if is_palindrome(new_nums):
            for i_ans in range(0,i):
                answer.append(digits[i_ans])
            answer.reverse()
            break
        new_nums = []

    print(f'Исходный список {digits}')
    print(f'Нужно чисел для палиндрома {len(answer)}')
    print(f'Сами числа {answer}')
#e
