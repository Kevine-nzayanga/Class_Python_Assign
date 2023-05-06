class Fruit:
    place="Supermarket"
    def __init__(self,name,family,number):
        self.name=name
        self.family=family
        self.number=number
    def increase(self):
     return self.number+1  
    def family_line(self):
       return (f"This is from the {self.family} family")
    def description(self):
       return(f"This {self.name} is from the {self.family} family.")      

apple=Fruit("Apple","Rosacea",23)      
print(apple.increase()) 
print(apple.family_line())
print(apple.description())