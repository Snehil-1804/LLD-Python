from typing import List

class Engine:
    def __init__(self,EngineType:str,horshpower:int)->None:
        self.__enginetype=EngineType
        self.__horshpower=horshpower

    def get_details(self)->str:
        return f"{self.__enginetype} engine ({self.__horshpower})"

    def start(self)->None:
        print(f"{self.__enginetype} engine started")

class Car:
    def __init__(self,brand:str,model:str,EngineType:str,horshpower:int)->None:
        self.__brand=brand
        self.__model =model

        self.__engine=Engine(EngineType,horshpower)

    def getCarDetails(self):
        print(f"\n Car: {self.__brand} {self.__model}")
        print(f"Engine: {self.__engine.get_details()}")

    def start(self):
        print(f"\n Starting {self.__brand} {self.__model}")
        self.__engine.start()
        print(f"Car is ready to drive....")

my_car:Car=Car("Toyota","hilux",'Diesel',204)

print("Before deleting the Car object")
my_car.getCarDetails()
my_car.start()
print("After deleting the Car object")
del my_car
print("\n Destroying the car...")