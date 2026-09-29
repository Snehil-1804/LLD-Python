from abc import ABC, abstractmethod

class Eatable:
    @abstractmethod
    def eat(self):
        pass

class Workable:
    @abstractmethod
    def work(self):
        pass

class Robot(Workable):
    def work(self):
        print("Robot is working")

class Employee(Eatable,Workable):
    def eat(self):
        print("Employee is working") 

    def work(self):
        print("Employee is working")        

e=Employee()
e.eat()
e.work()
r=Robot()
r.work()