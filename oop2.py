#section 2: functions in classes


#position , name, age , level , salary
se1 = ["Software Engineer", "Max", 20, "Junior", 5000]
se2 = ["Software Engineer", "somi", 20, "Junior", 5000]
se3 = ["Software Engineer", "somi", 20, "Junior", 5000]
d1 = ["Designer","Usama"]
def code(se):
    print(f"{se[1]} is writing a code")
    
code(d1)


#class
class SoftwareEngineer:
    alias = "Keyboard Magician"
    
    def __init__(self, name, age, level, salary):
        #instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
    
    #instance method
    def code(self):
        print(f"{self.name} is writing a code")
    
    def code_in_language(self,language):
        print(f"{self.name} is writing a code in {language}")
        
    #def information(self):
    #    information = f"name = {self.name}, age = {self.age}, level = {self.level}"
    #    return information
    
    # dunder method
    def __str__(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return information
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
    @staticmethod
    def entry_salary(age):
        if age > 25:
            return 5000
        if age < 30:
            return 8000
        return 9000
        

#instance
se1= SoftwareEngineer("ali",22,"junior",2000)
#print(se1.name,se1.age)
#print(SoftwareEngineer.alias)
se2= SoftwareEngineer("Usama",25,"Senior",5000)
se3= SoftwareEngineer("Usama",25,"Senior",5000)

#print(se2.name,se2.age)
#print(SoftwareEngineer.alias)



se1.code()
se2.code()
se1.code_in_language("Python")
se2.code_in_language("C++")

#print(se1.information())

print(se1)

print(se1.entry_salary(54))

print(SoftwareEngineer.entry_salary(22))