# 1) Update the Student Class to include these attributes - first_name, last_name, age, country
#      - Add these methods to the Student class
#              - show_full_name
#              - year_of_birth
#              - show_initials
class Students:
    school="Akirachix"
# Class methods
    def __init__(self,name,first_name,last_name,age,country,nationality):
        self.name=name
        self.age=age
        self.nationality=nationality
        self.first_name=first_name
        self.last_name=last_name
        self.country=country

    def show_initials(self):
        return(f"{self.first_name[0]},{self.last_name[0]}")
    def show_full_name(self):
        return(f"{self.first_name}, {self.last_name}")   

    def greet_student(self):
        return (f"Hello {self.name} welcome to {self.school}") 
    def year_of_birth(self):
        year=2023-self.age
        return f"Hello{self.name},you were born in {year}" 
    
Kevine=Students(name="Kevine",first_name="Keke",last_name="Nzayanga",age=21,country="Burunndi",nationality="Burundian")
Liza=Students(name="Eliza",first_name="Eliza",last_name="Ngambi",age=22,country="Kenya",nationality="Kenyan")    
Eunice=Students(name="Eunice",first_name="Mwiza",last_name="Ikirezi",age=23,country="Rwanda",nationality="Rwandan")  
print(Kevine.nationality)
print(Liza.school)
print(Liza.show_initials())
print(Eunice.show_full_name())
print(Kevine.greet_student())
print(Eunice.year_of_birth())








