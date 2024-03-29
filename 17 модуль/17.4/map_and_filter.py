# def from_string_(cls, date_as_string: str) -> 'Date':
#     day, month, year = map(int, date_as_string.split('-'))
#     date = cls(day, month, year)

from typing import List
from random import randint

nums1 = [randint(1, 10) for _ in range(10)]
nums2 = [randint(1, 10) for _ in range(10)]
print(nums1)
print(nums2)

result: List[int] = list(map(lambda a, b: a + b, nums1, nums2))    
print(result)

evens: List[int] = list(filter(lambda x: x % 2 == 0, result))
print(evens)

result = map(lambda num: num*3, filter(lambda num: num % 2 == 0, nums1))
print(list(result))