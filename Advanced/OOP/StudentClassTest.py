from Oops.StudentClass import Student


stu1 = Student(name="Maneesh", age=23, branch="CSE", sex="M")
stu2 = Student(name="Kaushik", age=24, branch="MEC", sex="M")
stu3 = Student(name="Rahul", age=23, branch="ECE", sex="M")
stu4 = Student(name="Shivani", age=22, branch="CSE", sex="F")
stu5 = Student(name="Soumya", age=26, branch="ISE", sex="F")

stu1.give_marks(69.69)
stu2.give_marks(60.60)
stu3.give_marks(78.78)
stu4.give_marks(80.80)
stu5.give_marks(69.69)

students = [stu1, stu2, stu3, stu4, stu5]

print("Name\t\tAge\t\tSex\t\tBranch\tCollege\t\tMarks")
print("-" * 55)
for student in students:
    print(student.get_name() + "\t\t" +
          str(student.get_age()) + "\t\t" +
          student.get_sex() + "\t\t" +
          student.get_branch() + "\t\t" +
          student.get_college() + "\t" +
          str(student.get_marks()))
