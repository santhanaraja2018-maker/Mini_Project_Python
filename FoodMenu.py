from AbstractItem import AbstractItem
from FoodItems import FoodItems

class FoodMenu(AbstractItem):

    def __init__(self,name):
        super().__init__(name = name)
        self.__FoodItems = []
    
    @property           #getter
    def FoodItems(self):
        return self.__FoodItems
    

    @FoodItems.setter
    def FoodItems(self, items):
        for item in items:
            if not isinstance (item, FoodItems):
                print("Invalid Food Items...")
                return
            
        self.__FoodItems = items

            


