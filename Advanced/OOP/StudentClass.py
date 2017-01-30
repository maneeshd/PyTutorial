class Student(object):
    def __init__(self, name, branch, sex, age):
        self.name = name
        self.branch = branch
        self.sex = sex
        self.age = age
        self.marks = 0
        self.college = "SIR MVIT"

    def give_marks(self, marks):
        self.marks = marks

    def get_marks(self):
        return self.marks

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_branch(self, branch):
        self.branch = branch

    def get_branch(self):
        return self.branch

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_sex(self, sex):
        self.sex = sex

    def get_sex(self):
        return self.sex

    def get_college(self):
        return self.college
