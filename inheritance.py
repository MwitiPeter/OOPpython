#single inheritance
# class Vehicle: #parentclass
#     def Vehicle_info(self):
#         print ('Inside Parent(Vehicle) class')

# class Car(Vehicle):#childclass
#     def Car_info(self):
#         print ('inside child (Car)class')

# car = Car()
# car.Vehicle_info()
# car.Car_info()

#Multiple Inheritance
# class Person: # parent 1
#     def person_info(self,name,age):
#         print('Inside the person class')
#         print('Name:',name,'age:', age)
# class Company: # parent 2
#     def company_info(self,company_name,location):
#         print ('inside company class')
#         print ('Name:', company_name,'location: ', location)
# class Employee (Person, Company): #child class
#     def  employee_info(self,salary,skill):
#         print('inside employee class')
#         print('Salary:', salary, 'Skill:', skill)

# emp=Employee() # creted an object
# emp.person_info('Zack',29)
# emp.company_info('meta','silicon valley')
# emp.employee_info(500000,'Software engineer')

#multilevel inheritance
# class Vehicles:#parent class
#     def vehicle_info(self):
#         print('inside vehicle class')
# class  Car(Vehicles):   
#     def car_info(self):
#         print ('inside the class car')
# class Bmw(Car):
#     def bmw_info(self):
#         print('inside bmwe class')

# bmw_car = Bmw()

# bmw_car.vehicle_info()
# bmw_car.car_info()
# bmw_car.bmw_info()

#hierarchical inheritance
# class Vehicle():
#     def info(self):
#         print ('this is a vehicle')
# class Car(Vehicle):
#     def car_info(self,name):
#         print ('care name :', name)
# class Truck(Vehicle):
#     def truck_info(self, name):
#         print ('truck name is:', name)  
# obj1 = Car()
# obj1.info()
# obj1.car_info('BMW')

# obj2 = Truck()
# obj2.info()
# obj2.truck_info('cyber')


#python super() function
class Company:
    def company_name(self):
        return 'google'
class Employee(Company):
    def info (self):
        c_name = super().company_name() 
        print("Jessa works at" , c_name)
emp = Employee()
emp.info()   
# issubclass() -In Python, we can verify whether a particular class is a subclass of another class. For this purpose, we can use Python built-in function issubclass(). This function returns True if the given class is the subclass of the specified class. Otherwise, it returns False.    