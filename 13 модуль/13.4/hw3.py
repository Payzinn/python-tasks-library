class Primes:
    def __init__(self, end):
        self.end = end
        self.start = 1
        self.prime_numbers = []

    def __iter__(self):
        self.start = 1
        return self
    
    def __next__(self):
        while self.start <= self.end:
            self.start += 1
            for prime in self.prime_numbers:
                if self.start % prime == 0:
                    break
            else:
                self.prime_numbers.append(self.start)
                return self.start
            
        raise StopIteration
    

my_iter = Primes(50)

for i in my_iter:
    print(i, end=' ')