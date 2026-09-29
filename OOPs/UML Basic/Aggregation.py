from typing import List

class Students:
    def __init__(self,name,roll_no)->None:
        self.__name = name
        self.__roll_no=roll_no

    def get_name(self)->str:
        return self.__name
    
    def get_roll_no(self)->int:
        return self.__roll_no

class Department:
    def __init__(self,dept_name)->None:
        self.__dept_name:str=dept_name
        self.__students:List[Students]=[]

    def add_student(self,student:Students):
        self.__students.append(student)

    def show_students(self)->None:
        print(f"\n Students in {self.__dept_name} Departments: ")
        for student in self.__students:
            print(f" -{student.get_name()}(Roll no: {student.get_roll_no()})")

rahul = Students("Rahul", 1)
priya = Students("Priya", 2)

cs_department = Department("Computer Science")
cs_department.add_student(rahul)
cs_department.add_student(priya)

cs_department.show_students()

del cs_department
print(rahul.get_name())