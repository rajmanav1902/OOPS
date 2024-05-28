'''A constructor is a special type of method (function) which is used to initialize the 
instance members of the class.'''

'''Constructors can be of two types.
1.Parameterized Constructor
2.Non-parameterized Constructor
Constructor definition is executed when we create the object of this class. 
Constructors also verify that there are enough resources for the object to perform any start-up task.'''

#In Python, the method the __init__() simulates the constructor of the class. 

#Parameterized constructor
class Employee:  
    def __init__(self, name, id):  
        self.id = id  
        self.name = name  
  
    def display(self):  
        print("ID: %d \nName: %s" % (self.id, self.name))  
  
emp1 = Employee("John", 101)  
emp2 = Employee("David", 102)    
emp1.display()  
emp2.display() 

#Non-parameterized: They can be used when we want to initialize an obect with default value
class Point:
  def __init__(self):  # Non-parameterized constructor
    self.x = 0
    self.y = 0

point1 = Point()  # Creates a point at (0, 0)

'''Note:When we do not include the constructor in the class or forget to declare it, 
then that becomes the default constructor. It does not perform any task but initializes the objects.'''

#Q) Can we have multiple constructors in a class?
'''Absolutely! Having multiple constructors in a class, also known as constructor overloading, 
is a common and powerful feature in object-oriented programming. 
It allows you to create objects in different ways depending on the information you have available.'''
class Person:
  def __init__(self, name): 
    self.name = name

  def __init__(self, name, age):
    self.name = name
    self.age = age
person1 = Person("Alice")
person2 = Person("Bob", 30)

print(person1.name)  
print(person2.name, person2.age)


