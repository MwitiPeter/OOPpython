# class A:
#     def __init__ (self):
#         self.count = 5
#         self.count= self.count+1
# a=A()
# print(a.count)      

# class A:
#     def __init__(self,num):
#         num=3
#         self.num = num
#     def change (self):
#             self.num=7
# a = A(5)
# print(a.num)  
# a.change()
# print (a.num)            


# class Student:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#         print(self.id)
# std = Student("Simon",1)   
# std.id = 2
# print(std.id)   


# class A():
#     def __init__(self,count=100):
#         self.count=count
# obj1=A()
# obj2=A(102)
# print (obj1.count) 
# print (obj2.count)     


# class A:
#     def __init__(self,name):
#         self.name=name
# a1=A("john") 
# a2=A("john") 
# print (a1.name)
# print(a2.name)      

class test:
    def __init__(self,a):
        self.a = a
    def display(self):
            print(self.a)
            
obj=test()
obj.display()             