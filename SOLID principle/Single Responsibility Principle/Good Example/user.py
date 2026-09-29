class User:
    def __init__(self,name:str,age:int,email:str)->None:
        self.__name=name
        self.__age=age
        self.__email=email

    def get_user_name(self)->str:
        return self.__name

    def get_user_age(self)->int:
            return self.__age

    def get_user_email(self)->str:
            return self.__email 