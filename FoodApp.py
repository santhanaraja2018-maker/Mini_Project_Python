from User import User
from UserManager import UserManger

class LoginSystem:

    def login(self):
        mailid = input("Enter your mail id : ")
        password = input("Enter Your PassWord : ")

        user = UserManger.find_user(mailid= mailid, password= password)

        if user is not None:
            print("You have successfully logged in")
            pass  #next step code here
        else:
            print("Invalid username or password")


    def register(self):
        name = input("Enter Name : ")
        mobile = int(input("Enter Mobile Number : "))
        mailid = input("Enter your mail id : ")
        password = input("Enter Your PassWord : ")

        userObj = User(name= name, phone= mobile, mail= mailid, password= password)
        UserManger.add_user(userObj)


    def guest_login(self):
        pass

    def exit_app(self):
        print("Thanks for visiting our Online Food Ordering System ")
        exit()  #it stops our program running

    def validate_options(self,option):

        if option == 1:
            self.login()
            
        elif option == 2:
            self.register()

        elif option == 3:
            self.guest_login()

        elif option == 4:
            self.exit_app()

        else :
            print("You have entered invalid input")




class FoodApp:

    login_options = { 1:"Login",
                      2: "Register", 
                      3 : "Guest", 
                      4 : "Exit" }

    @staticmethod
    def init():
        print ("Welcome to Online Food ordering System")
        # creating object
        loginsystem = LoginSystem()

        while True:   #until user exit the app the program should run 
            for key,value in FoodApp.login_options.items():
                print (f"{key}.{value}",end="  ")
                
            try:
                choice = int(input("\n Please Enter Your Choice : "))
                loginsystem.validate_options(choice)
                
            except ValueError:
                print("Please enter valid choice")
        