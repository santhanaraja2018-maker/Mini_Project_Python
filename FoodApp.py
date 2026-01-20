from User import User
from UserManager import UserManger
from MainMenu import MainMenu

class LoginSystem:

    def login(self):
        mailid = input("Enter your mail id : ")
        password = input("Enter Your PassWord : ")

        user = UserManger.find_user(mailid= mailid, password= password)

        if user is not None:
            print("You have successfully logged in")
            menu = MainMenu()
            menu.Start()

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

        # if option == 1:
        #     self.login()
            
        # elif option == 2:
        #     self.register()

        # elif option == 3:
        #     self.guest_login()

        # elif option == 4:
        #     self.exit_app()

        # else :
        #     print("You have entered invalid input")  

        # instead of if else we can use getattr by passing the value intead of choice

        getattr(self,option)()

        # here we use () to indicate methos if no () then it checks for variable




class FoodApp:

    login_options = { 1:"login",
                      2: "register", 
                      3 : "guest_login", 
                      4 : "exit_app" }

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
                loginsystem.validate_options(FoodApp.login_options[choice])   # if we use if else


                # alternate method
                # for getattr () we store choice in option and pass it to our method login options
                # option = FoodApp.login_options.get(choice)
                # if option:
                #     loginsystem.validate_options(option)
                # else:
                #     print("Please enter valid Option")
                
            except (ValueError,KeyError):
                print("Invalid Input... Please enter valid choice")
        