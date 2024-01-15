class User:
    user_name = 'Admin'
    password = 'qwerty'
    is_banned = False
    friends = []

    def print_info(self):
        print('Name: {}\nPassword: {}\nBan_status: {}'.format(
            self.user_name, 
            self.password, 
            self.is_banned)
            )
        
    def add_friend(self, friend):
        if isinstance(friend, User):
            self.friends.append(friend.user_name)
        else:
            self.friends.append(friend)


user_1 = User()
user_2 = User()
user_2.user_name = 'Alina'
user_1.user_name = 'Alloha'
user_1.print_info()
user_1.add_friend('Nicko')
user_1.add_friend(user_2)
print(user_1.friends)