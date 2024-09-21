#public access modifier
# class Student:
#     shoolName = 'PLP Academy' # class attribute

#     def __init__(self,name,age):
#         self.name=name #instance attribute
#         self.age= age# instance attribute
# std = Student("Mutuku", 23)
# print(std.shoolName)
# print(std.name)
# print(std.age )  


#protected members = Add an anderscore before it 
# class Student:
#     _schoolName = 'XYZ School'#protected class attribute

#     def __init__(self,name ,age):
#         self._name=name # aprotected instance attribute
#         self._age=age # protected instnce attribute
# std = Student("Tembo",25)  
# print (std._name)
# print (std._age)


#private member = use double underscore 
class Student:
    __schoolName = 'XYz'
    def __init__(self,name,age):
        self.__name = name#private instance attribute
        self.__salary = age#private instance attribute
    def __display(self): #private method
        print ('This is a private method')   
std = Student("Bill",25)
print(std._Student__name )
std._Student__display()       