class Persons:
    def __init__(self,name,age):#class constructor
        self.name=name
        self.age = age
    def displayInfo(self):#class method
        print('Persons name:',self.name,'age:',self.age)  
#calling the methods          
p1=Persons('Mwiti',20)
p1.displayInfo()
#deleting attribute
# del p1.age
# print(p1.age) 

#deleting objects
# del p1 
# print(p1.name)

#deleting class
# del Persons
