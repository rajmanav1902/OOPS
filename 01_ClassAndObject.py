'''A class is a user-defined data type that contains data members and the methods that may be used to manipulate it. 
In a sense, classes serve as a blueprint/template to create objects.'''

'''An object can be any real world entity. It has access to the data members of a class
An object can be defined as an instance of class.'''

'''Note:While creating an object assign value to the parameterized constructor'''

class Person:  #Defining a class
    def __init__(self, name, age):  #Constructor
        self.name = name    
        self.age = age      
    def greet(self):  
        print("Hello, my name is " + self.name)  
  
# Create a new instance of the Person class and assign it to the variable person1  
person1 = Person("Ayan", 25)  
person1.greet() #Access methods of a classs

'''The self-parameter refers to the current instance of the class and accesses the class variables. 
We can use anything instead of self, but it must be the first parameter of any function which belongs to the class.'''

#We can relate self of python to this of java

'''In order to make an instance of a class in Python, a specific function called __init__ is called. 
Although it is used to set the object's attributes, it is often referred to as a constructor.'''