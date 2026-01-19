from User import User

class UserManger():
    __Users=[]

    @classmethod
    def add_user(cls, userObj):

        if isinstance(userObj,User):    # it checks whether the passed userObj is object of User class 
            cls.__Users.append(userObj)
            print("You have been successfully registered")
        
        else:
            print("Invalid Credentials")
    
    @classmethod
    def find_user (cls, mailid, password):
        for user in cls.__Users:
            if user.Email == mailid and user.Password == password:
                return user
