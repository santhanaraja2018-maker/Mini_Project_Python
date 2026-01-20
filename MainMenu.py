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

        name= input("Please Select Restaurant ").strip().casefold()
        res = self.__FoodManager.FindRestaurant(name)
        if res is not None:
            self.ShowFoodMenus(res.FoodMenus)
        else:
            print("Restaurant not found")



    def ShowFoodItems (self, foodItems = None):
        
        if isinstance(foodItems, list) and foodItems and isinstance(foodItems[0], FoodMenu):
            items = []
            for menu in foodItems:
                items.extend(menu.FoodItems)
                foodItems = items

        if foodItems is None:
            foodItems = []

            for res in self.__FoodManager.Restaurants:
                for menu in res.FoodMenus:
                    foodItems.extend(menu.FoodItems)

        if not foodItems:
            print("No food items available")
            return
        
        print("\n Available Food Items \n")
        for index,item in enumerate(foodItems,start=1):
            print(f"{index}. {item.Name} | "
                  f"Rating :{item.Rating} | "
                  f"Price : {item.Price} | "
                  f"Description : {item.Description}"
                  )
        


        

    def SearchRestaurant (self):
        resName = input ("Enter Restaurant Name : ").strip().casefold()
        res= self.__FoodManager.FindRestaurant(resName)

        if res is not None:
            print(f"Name : {res.Name}, Rating : {res.Rating}")
            self.ShowFoodMenus(res.FoodMenus)

        else :
            print(f"No Restaurant found on the name {resName}")

    def SearchFoodItems (self):
        pass

    def ShowFoodMenus(self, menus):
        if menus is not None:
            self.ShowFoodItems(menus)
        
        else:
            print("No Food Avilable in this Restaurant")

    def logout(self):
        print("Thanks for visiting our Online Food Ordering System ")
        exit()
    
    
    def Start(self):

        while True:
            for key,value in MainMenu.__Options.items():
                print (f"{key}.{value}", end="  ")

            try:
                choice = int (input ("\nPlease Enter Your Choice : "))
                value = MainMenu.__Options[choice].replace(" ","")
                getattr(self,value)()

            except(ValueError,KeyError):
                print("Inavlid input .. Please Enter Valid Choice")