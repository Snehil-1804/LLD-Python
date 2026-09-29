from user import User
from userRepositiory import UserRepositiory

user_obj=User("Snehil Priyam",21,"info@gmail.com")
userRepositiory_obj=UserRepositiory("userDB","root","root")


print(user_obj.get_user_name())

userRepositiory_obj.save_to_db(user_obj)