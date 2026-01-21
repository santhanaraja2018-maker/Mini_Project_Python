from AbstractItem import AbstractItem
from FoodMenu import FoodMenu

class Restaurant(AbstractItem):

    def __init__(self,name,rating,location,offer):
        super().__init__(name = name,rating = rating)
        self.Location = location
        self.Offer = offer
        self.__FoodMenus = []


    @property
    def FoodMenus(self):
        return self.__FoodMenus
    
    @FoodMenus.setter
    def FoodMenus (self,items):
        for item in items:
            if not isinstance (item, FoodMenu):
                print("Invalid Food Items...")
                return
            
        self.__FoodMenus = items

         
 