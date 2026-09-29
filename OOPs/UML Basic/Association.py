class Teacher:
    def __init__(self,name:str)->None:
        self.__name:str=name

    def get_name(self)->str:
        return self.__name

    def teach(self,students:"Students")->None:
        print(f"{self.__name} is teaching {students.get_name()}")
         
class Students:
    def __init__(self,name:str)->None:
            self.__name:str=name
    
    def get_name(self)->str:
        return self.__name

teacher1 = Teacher("Hemanta")
students1= Students("Snehil")
teacher1.teach(students1)