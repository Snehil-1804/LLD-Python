class User:
    def __init__(self,name:str,age:int,email:str)->None:
        self.__name=name
        self.__age=age
        self.__email=email

    def get_user_name(self)->str:
        return self.__name

    def get_user_age(self)->int:
            return self.__age

    def get_user_name(self)->str:
            return self.__email

    def save_to_database(self):
          return f"{self.user} details are getting saved to the database"

    def delete_to_database(self):
              return f"{self.user} details are getting delete from the database"
    