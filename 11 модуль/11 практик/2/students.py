import random
from random import choice

class Student:
    def __init__(self, name_surname, group, grade):
        self.name_surname = name_surname
        self.group = group
        self.grade = grade

    def __str__(self):
        return "ФИ: {}\tГруппа: {}\tУспеваемость: {}".format(self.name_surname, self.group, self.grade)
    
    def get_average_grade(self):
        return sum(self.grade) / len(self.grade)
    
    def sort_students(students):
        sorted_students = []
        while students:

            best_student = None
            best_grade = 0

            for student in students:
                if student.get_average_grade() > best_grade:
                    best_student = student
                    best_grade = student.get_average_grade()
            
            sorted_students.append(best_student)
            students.remove(best_student)

        return sorted_students[::-1]

students = []

names = [
    "Иванов Иван",
    "Петров Пётр",
    "Сидоров Сидор",
    "Васильев Василий",
    "Кузнецов Кузьма",
    "Соколов Сокол",
    "Попов Поп",
    "Михайлов Михаил",
    "Андреев Андрей",
    "Семёнов Семён",
    "Егоров Егор",
    "Павлов Павел",
    "Николаев Николай",
    "Александров Александр",
    "Сергеев Сергей",
    "Фёдоров Фёдор",
    "Тарасов Тарас",
    "Емельянов Емельян",
    "Яковлев Яков",
    "Степанов Степан",
]



for people in range(10):
    name_surname = random.choice(names)
    group = random.randint(100, 1000)
    grades = [random.randint(2,5) for _ in range(5)]
    students.append(Student(name_surname, group, grades))


sorted_students = Student.sort_students(students)

for man in sorted_students:
    print(man.name_surname, man.group, man.get_average_grade())
