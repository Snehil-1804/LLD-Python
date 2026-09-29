from user import User

class UserRepositiory:
    def __init__(self,db,username,password):
        self.__db=db
        self.__username=username
        self.__password=password

    def save_to_db(self,user:"User"):
        print(f"{user.get_user_name()} is getting saved to the database.")

    def delete_from_db(self,user:User):
        return f"{user.get_user_name()} is getting deleted from the database."