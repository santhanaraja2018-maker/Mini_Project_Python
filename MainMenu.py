from FoodManager import FoodManager
from FoodMenu import FoodMenu


class MainMenu:

    __Options = {1: "Show Restaurants", 2: "Show FoodItems", 3: "Search Restaurant", 4: "Search FoodItems",5: "logout"}

    def __init__(self):
        self.__FoodManager =  FoodManager()


    def ShowRestaurants (self):

        print("\n Available Restaurants \n")
        for res in self.__FoodManager.Restaurants:
            print (f">> {res.Name} => Rating : {res.Rating}")

        name= input("\nPlease Select Restaurant : ").strip().casefold()
        res = self.__FoodManager.FindRestaurant(name)
        if res is not None:
            print("\nThank You for choosing ",name.upper())
            self.ShowFoodMenus(res.FoodMenus)
        else:
            print("Restaurant not found")



    def ShowFoodItems (self, foodItems = None):

        if foodItems is None:
            foodItems = []

            for res in self.__FoodManager.Restaurants:
                for menu in res.FoodMenus:
                    foodItems.extend(menu.FoodItems)

        if not foodItems:
            print("No food items available")
            return
        
        print("\n Available Food Items \n")
        for i,item in enumerate(foodItems,start=1):
            print(f"{i}. {item.Name} | "
                  f"Rating :{item.Rating} | "
                  f"Price : {item.Price} | "
                  f"Description : {item.Description}"
                  )
        


        

    def SearchRestaurant (self):
        resName = input ("Enter Restaurant Name : ").strip().casefold()
        res= self.__FoodManager.FindRestaurant(resName)

        if res is not None:
            print("\nRestaurant Found, Happy Ordering \n")
            print(f"Name : {res.Name}, Rating : {res.Rating}")
            self.ShowFoodMenus(res.FoodMenus)

        else :
            print(f"No Restaurant found on the name {resName}")

    def SearchFoodItems (self):

        while True:
            food = input("\nEnter food you like or enter 0 to go back : ").strip().casefold()

            if food != "0":
                results = self.__FoodManager.FindFood(food)

                if results:
                    print("\nYour food is here\n")
                    print(f"Name : {results.Name} | Price: {results.Price} | Rating : {results.Rating}")

                else :
                    print(f"No food found on the name {food}")
            else :
                break



    def ShowFoodMenus(self, menus):

        if not menus:
            print("No Food Avilable in this Restaurant")
            return
        
        while True:
            
            print("Avilable Food Menus \n" )
            for i,menu in enumerate(menus,1):
                print(f"{i}. {menu.Name}")

            try:
                print("\n To search other restaurants enter 0 \n")
                choice = int(input("Please Choose Menu : "))

                if choice ==0:
                    break

                if (choice>0 and choice<=len(menus)):
                    fooditems = menus[choice-1].FoodItems
                    print("\n To search other restaurants enter 0 \n")
                    self.ShowFoodItems(fooditems)

                else:
                    print ("\nPlease enter valid Choice\n")

            except ValueError:
                print("\n Please enter number only\n")
            

    def logout(self):
        print("Thanks for visiting our Online Food Ordering System ")
        exit()
    
    
    def Start(self):

        while True:
            print()
            for key,value in MainMenu.__Options.items():
                print (f"{key}.{value}", end="  ")

            try:
                choice = int (input ("\nPlease Enter Your Choice : "))
                value = MainMenu.__Options[choice].replace(" ","")
                getattr(self,value)()

            except(ValueError,KeyError):
                print("Inavlid input .. Please Enter Valid Choice")