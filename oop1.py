

#position , name, age , level , salary
se1 = ["Software Engineer", "Max", 20, "Junior", 5000]
se2 = ["Software Engineer", "somi", 20, "Junior", 5000]



#class
class SoftwareEngineer:
    alias = "Keyboard Magician"
    
    def __init__(self, name, age, level, salary):
        #instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
        
        

#instance
se1= SoftwareEngineer("ali",22,"junior",2000)
print(se1.name,se1.age)
#print(SoftwareEngineer.alias)
se2= SoftwareEngineer("Usama",25,"Senior",5000)
print(se2.name,se2.age)
#print(SoftwareEngineer.alias)

