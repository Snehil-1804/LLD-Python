class Animal:
    def __init__(self,name:str,age:int)->None:
        self.name=name
        self.age=age

    def eat(self):
        print("I am eating...")

    def sleep(self):
        print("I am sleeping...")
class Dog(Animal):
    def __init__(self, name:str, age:str, breed:str):
        super().__init__(name, age)
        self.breed=breed

    def bark(self):
        print("I am barking...")

    def display(self):
        print(f"Name is {self.name} and age is {self.age} and the breed {self.breed}")

dog=Dog("Bruno",5,"Indie")
dog.display()