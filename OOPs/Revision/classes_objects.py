class Students:
    def __init__(self, name:str, age:int, gender:str) -> None:
        self.name=name
        self.age=age
        self.gender=gender

    def display(self) -> str:
        return f"name: {self.name}, age: {self.age}, gender: {self.gender}"

    def get_age(self)->int:
        return self.age

s1=Students("Snehil",21,"Male")
print(s1.display())
print(s1.get_age())