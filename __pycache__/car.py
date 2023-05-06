class Car:
    wheels=2
    def __init__(self, milleage,type,model):
          self.milleage=milleage
          self.type=type
          self.model=model
    def cover(self,distance):
        return self.milleage*distance
    def types(self):
         return (f"THis car is {self.type}")

    def details(self):
         return(f"This car is {self.type} of {self.model}")
    
Toyota=Car(200,"Mistu","maca")  
print(Toyota.types())
print(Toyota.cover(12))
print(Toyota.details())  
               