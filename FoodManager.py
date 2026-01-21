from FoodItems import FoodItems
from Restaurant import Restaurant
from FoodMenu import FoodMenu

class FoodManager:

    def __init__(self):
        self.Restaurants = self.__PrepareRestaurants()
        self.FoodItems = self.__PrepareFoodItems()
        



    def __PrepareFoodItems(self):
        item1 = FoodItems(name= "VegBriyani",rating= 4.4, price= 140, description= "Seeragasamba")
        item2 = FoodItems(name= "ChickenBriyani",rating= 4.6, price= 150, description= "Seeragasamba")
        item3 = FoodItems(name= "MuttonBriyani",rating= 4.8, price= 200, description= "Seeragasamba")
        item4 = FoodItems(name= "BeafBriyani",rating= 4.7, price= 240, description= "Seeragasamba")
        item5 = FoodItems(name= "KaadaiBriyani",rating= 4.5, price= 210, description= "Seeragasamba")
        item6 = FoodItems(name= "NanduBriyani",rating= 4.9, price= 260, description= "Seeragasamba")

        return [item1, item2, item3, item4, item5, item6]


    def __PrepareFoodMenus(self):
        FoodItems = self.__PrepareFoodItems()
        menu1 = FoodMenu("Veg")
        menu1.FoodItems = [FoodItems[0]]

        menu2 = FoodMenu("Non - Veg")
        menu2.FoodItems = [FoodItems[1],FoodItems[4],FoodItems[3],FoodItems[2]]

        menu3 = FoodMenu("Chinese")
        menu3.FoodItems = [FoodItems[5]]

        return [menu1,menu2,menu3]
        
    def __PrepareRestaurants(self):
        FoodMenus = self.__PrepareFoodMenus()

        res1 = Restaurant (name= "A2B",rating= 4.8, location= "Chennai", offer= 10)
        res1.FoodMenus=self.__PrepareFoodMenus()

        res2 = Restaurant (name= "KFC",rating= 4.5, location= "Madurai", offer= 20)
        res2.FoodMenus=self.__PrepareFoodMenus()

        res3 = Restaurant (name= "Adyar Aananda Bhavan",rating= 4.2, location= "Adyar", offer= 15)
        res3.FoodMenus=self.__PrepareFoodMenus()

        return [res1,res2,res3]
    
    def FindRestaurant(self,name):
        for res in self.Restaurants:
            if res.Name.casefold() == name:
                return res
            

    def FindFood(self,name):
        for food in self.FoodItems:
            if food.Name.casefold()==name:
                return food

