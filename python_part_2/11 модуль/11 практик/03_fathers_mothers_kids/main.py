class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.kids = []

    def __str__(self):
        return "Имя: {}, возраст: {}".format(self.name, self.age)

    def calm_kid(self, kid):
        kid.calm()

    def feed_kid(self, kid):
        kid.feed()

class Kid:
    def __init__(self, name, age, calm_status = True, hungry_status = True):
        self.name = name
        self.age = age
        self.calm_status = calm_status
        self.hungry_status = hungry_status

    def __str__(self):
        return "Имя: {}, возраст: {}, спокойствие: {}, голод: {}".format(self.name, self.age, self.calm_status, self.hungry_status)

    def calm(self):
        self.calm_status = True
        print('Теперь {} спокоен'.format(self.name))

    def feed(self):
        self.hungry_status = False
        print('Теперь {} не голоден'.format(self.name))

parent = Parent('Thomas', 55)
child = Kid('Robert', 15)

parent.kids.append(child)
parent.feed_kid(child)
parent.calm_kid(child)
print(parent)
print(child)