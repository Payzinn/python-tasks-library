def first():
    def fact(num):
        if num == 1:
            return 1
        
        return fact(num - 1) * num
    
    print(fact(5))


def second():
    def fibonacci(num):
        if num == 1:
            return 0
        elif num == 2:
            return 1

        return fibonacci(num - 1) + fibonacci(num - 2)