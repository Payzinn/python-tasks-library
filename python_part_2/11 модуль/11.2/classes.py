class User:
    user_name = 'Admin'
    password = 'qwerty'
    is_banned = False

user_1 = User() # Экземпляр класса User
user_1.user_name = 'Tom'
print(user_1.user_name)

user_2 = User()
print(user_2.user_name)