def fibonacci(number):
    cur_val = 0
    next_val = 1
    for _ in range(number):
        yield cur_val
        cur_val, next_val = next_val, cur_val + next_val
        if cur_val > 10 ** 6:
            return

def square(nums):
    for num in nums:
        yield num ** 2

fib_seq = fibonacci(number=10)
for i in fib_seq:
    print(i)

print("\n")
print(sum(square(fibonacci(number=5000))))

print()

cubes_gen = (num ** 3 for num in range(10))
for i_num in cubes_gen:
    print(i_num, end=' ')