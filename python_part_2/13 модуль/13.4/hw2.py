import random

class SumOfTwo:
    def __init__(self, end):
        self.counter = 0
        self.last = 0
        self.end = end

    def __iter__(self):
        self.counter = 0
        self.last = 0
        return self
    
    def __next__(self):
        self.counter += 1
        if self.counter > self.end:
            raise StopIteration
        else:
            self.last += random.random()
            return self.last
        

m = SumOfTwo(5)
for i in m:
    print(round(i, 2))
        
print()

for i in m:
    print(round(i, 2))

print()
      
for i in m:
    print(round(i, 2))
        