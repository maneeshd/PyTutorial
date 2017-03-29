"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@date: 3/29/2017
"""
from os import urandom
from Advanced.OOP.Inheritance.Base import Student


class MyClass(Student):
    secret_key = urandom(8)

    @classmethod
    def get_secret_key(cls):
        return cls.secret_key

    def __init__(self, name, age, sex, grade):
        super().__init__(name, age, sex)
        self.grade = grade

    def get_details(self):
        return super().get_details() + "\nGrade:\t" + self.grade + "\n"


def main():
    print("Secret Key1 = {0}".format(Student.get_secret_key()))
    print("Secret Key2 = {0}".format(MyClass.get_secret_key()))
    print("")
    student1 = MyClass("Maneesh", 24, "Male", "A")
    student2 = MyClass("Soumya", 27, "Female", "A+")
    print(student1.get_details())
    print(student2.get_details())

if __name__ == '__main__':
    main()

