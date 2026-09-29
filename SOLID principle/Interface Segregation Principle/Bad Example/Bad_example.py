from abc import ABC, abstractmethod

class Employee:

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def work(self):
        pass

class Worker(Employee):
    def eat(self):
        print("Worker is eating")

    def work(self):
        print("Worker is working")

class Robot(Employee):
    def eat(self):
        raise Exception("Robot can't eat")

    def work(self):
        print("Robot is working")

r=Robot()
r.work()
r.eat()
