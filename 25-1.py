#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from random import randint


class User(ABC):

    id = 1

    @abstractmethod
    def __init__(self, name):
        self.id = User.id
        User.id += 1
        self.name = name
        self.courses = []


class Teacher(User):

    def __init__(self, name, degree):
        super().__init__(name)
        self.degree = degree

    def check_homework(self, course):
        for lesson in course.lessons:
            for i in lesson.homework:
                if len(lesson.homework[i]) == 1:
                    lesson.homework[i].append(randint(2, 5))
                else:
                    lesson.homework[i][1] = randint(2, 5)


class Student(User):

    def __init__(self, name, group):
        super().__init__(name)
        self.group = group

    def upload_homework(self, lesson, work):
        if self not in lesson.homework:
            lesson.homework[self] = []
        lesson.homework[self][0] = [work]


class Course:

    id = 1

    def __init__(self, name):
        self.id = Course.id
        Course.id += 1
        self.name = name
        self.teachers = []
        self.students = []
        self.lessons = []

    def __str__(self):
        teachers = '\n'.join([f'{i.degree} {i.name}' for i in self.teachers])
        students = '\n'.join([f'{i.group} {i.name}' for i in self.students])
        lessons = '\n'.join([f'Занятие №{i.number} - {i.topic}'
                             for i in self.lessons])
        str = (self.name + '\nПреподаватели курса:\n' + teachers
               + '\nСтуденты курса:\n' + students + '\nЗанятия:\n' + lessons)
        return str

    def assign_to_course(self, *users):
        for user in users:
            if isinstance(user, (Teacher, Student)):
                user.courses.append(self)
                if isinstance(user, Student):
                    self.students.append(user)
                else:
                    self.teachers.append(user)
            else:
                print('Вы кто вообще?')

    def create_lesson(self, *topics):
        for topic in topics:
            self.lessons.append(Lesson(self, topic))

    def check_progress(self):
        progress = {}
        for student in self.students:
            grade = 0
            for lesson in self.lessons:
                if student not in lesson.homework:
                    lesson.homework[student] = ['Долг', 2]
                grade += lesson.homework[student][1]
            grade = round(grade/len(self.lessons))
            progress[student.name] = grade
        return progress


class Lesson:

    id = 1

    def __init__(self, course, topic):
        self.__id = Lesson.id
        Lesson.id += 1
        self.number = len(course.lessons) + 1
        self.topic = topic
        self.homework = {}


def random_homework(student, course):
    completed = [randint(0, 1) for i in range(len(course.lessons))]
    for i, j in enumerate(completed):
        if j:
            course.lessons[i].homework[student] = [5*chr(randint(65, 90))]


marvanna = Teacher('Косолапова М.И.', 'Старший учитель')
vovochka = Student('Ножкин В.В.', '5А')
ego_drug = Student('Ложкин Г.Г.', '5А')
math = Course('Математика')
math.assign_to_course(marvanna, vovochka, ego_drug)
math.create_lesson('Сложение', 'Вычитание', 'Умножение', 'Деление',
                   'Комплексные числа')
print(math, end=2*'\n')
random_homework(vovochka, math)
random_homework(ego_drug, math)
marvanna.check_homework(math)
progress = math.check_progress()
print('Итоги по курсу:')
for name, value in progress.items():
    print(name, value)
