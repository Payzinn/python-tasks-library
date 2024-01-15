class User:
    user_name = 'Admin'
    password = 'qwerty'
    is_banned = False

user_1 = User() # Экземпляр класса User
user_2 = User()
user_2.user_name = 'Tom'
print(user_1.user_name, user_2.user_name)
User.user_name = 'NoName'
print(user_1.user_name, user_2.user_name)
