    #class attributes
# class Person:
#     name = "skinny"
# print(Person.name)
# details = Person()
# print(details.name)

     #class constructor

# class Person:
#     def __init__(self):#constructor method
#      print('Constructor invoked')
# details1 = Person()
# details2 = Person()

       #insatce attruibutes

class Person:
    nationality = 'Ethopia'# class attribute
# default values of instance variable 
    def __init__(self,name="mkuu", age=101):
                 self.name = name
                 self.age=age
p1 = Person()
print(p1.name)
print(p1.age)                 
#setting attributesvalues    
#     def __init__(self,name,age) :
#         self.name = name
#         self.age = age
# p1=Person('Muteti',45)
# print(p1.name)
# print(p1.age) 

      
#     def __init__(self):# constructor
#         self.name = ''#instance ayttribute
#         self.age = 0 #instance attribute
# p1=Person()#instancename
# p1.name="Mwiti"
# p1.age =20
# print(p1.name)
# print(p1.age)

