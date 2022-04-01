

class Drink:
    def __init__(self, name, quantity):
        self.name = name
        self.__quantity = quantity
        
    def getName(self) :
        return self.name
    
    def getQuantity(self) :
        return self.__quantity
    
    def set_quantity(self , q) : 
        self.__quantity = q
        
    def ToString(self) :
        return "You have {0} unit of {1}".format(self.__quantity, self.name)
    
    def shot(self, dose) : 
        if dose >= self.__quantity :
            print("You don't have enough of", self.name , "for your shot so you empty your glass")
            self.__quantity = 0
        elif dose < self.__quantity :
            print("you drink a shot of", dose, "unit of", self.name )
            self.__quantity -= dose
            
        

class Bottle(Drink):
    
    def __init__(self, name, quantity, price):
        super().__init__(name,quantity)
        self.__quantityOfOne = 1.5
        self.price = price
        self.__quantity = quantity
        
    def getQuantityOfOne(self) :
        return self.__quantityOfOne
        
    def howMany(self):
        if (self.__quantity % self.__quantityOfOne) == 0:
            return round(self.__quantity / self.__quantityOfOne)
        else : 
            return round(self.__quantity / self.__quantityOfOne)+1
    
    def howMuch(self):
        return (self.howMany()*self.price)
    
    def ToString(self):
        return "For {0}L of {1}, we need {2} bottles. It will cost {3}".format(self.__quantity, self.name, self.howMany(), self.howMuch())








        
                
bibine = Bottle('rum', 6, 13)

print(bibine.ToString())
