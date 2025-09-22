#oops is a object oriented programming system which is used to reduce the redudency and increse the reuseabaility....,
#it is a programming paradigm which is used to solve the complex problems in a simple way by using the real world entities 
# like object, class, inheritance, polymorphism, encapsulation, abstraction etc....
#class is a blueprint of an object which is used to create the object and it contains the attributes and methods of the object...
#object is an instance of a class which is used to access the attributes and methods of the class...
#syntax of class:
#class class_name:
class student:
    name = "puneeth_k"
    age = 21

s1 = student()
print(s1.name)

s2 = student()
print(s2.age)

#constructor is a special method which is used to initialize the attributes of the class...
class car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

c1 = car("BMW", "X5", 2020)
print(c1.name)

c2 = car("Audi", "A6", 2021)
print(c2.model)

c3 = car("Mercedes", "C-Class", 2022)
print(c3.year)

#

class car:
    object_type = "vehicle" # its like a global variable,,,,,
    def __init__(self, name, model, year):
        self.name = name #its like a local variable,,,,
        self.model = model
        self.year = year

c1 = car("BMW", "X5", 2020)
print(c1.name)
print(c1.object_type) 

c2 = car("Audi", "A6", 2021)
print(c2.model)

c3 = car("Mercedes", "C-Class", 2022)
print(c3.year)

#method is a function which is defined inside the class and it is used to perform some operations on the attributes of the class...
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):   #methode
        print("Name:", self.name)
        print("Age:", self.age)

p1 = person("John", 25)
p1.display()

#use staticmethode to minimize the use of self

#abstraction is a process of hiding the implementation details and showing only the functionality to the user...


#encapsulation is a process of wrapping the data and methods into a single unit...