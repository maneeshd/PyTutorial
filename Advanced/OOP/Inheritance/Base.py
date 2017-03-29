"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@date: 3/29/2017
"""
from os import urandom
from secrets import SystemRandom


class Student:
    secret_key = urandom(8)

    @classmethod
    def get_secret_key(cls):
        return cls.secret_key

    def __init__(self, name: str, age: int, sex: str):
        rand = SystemRandom()
        self.name = name
        self.age = age
        self.sex = sex
        self.UID = "%s%d" % (name[:4], rand.choice(range(1010, 9090)))

    def get_details(self):
        return "Name:\t%s\nAge:\t%d\nSex:\t%s\nID:\t\t%s" % (self.name, self.age, self.sex, self.UID)
