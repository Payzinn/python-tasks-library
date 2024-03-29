from typing import List

users: List = ['user100', 'user5', 'user4', 'user22', 'user9']
sorted_users = sorted(users, key = lambda elem: int(elem[4:]))
print(sorted_users)

x = lambda a: a + 10
print(x(5))