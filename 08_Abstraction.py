'''Abstraction is used to hide the internal functionality of the function from the users. 
The users only interact with the basic implementation of the function, but inner working is hidden. 
User is familiar with that "what function does" but they don't know "how it does."'''

'''Note:
An Abstract class can contain the both method normal and abstract method.
An Abstract cannot be instantiated; we cannot create objects for the abstract class.'''

'''Syntax:
from abc import ABC  
class ClassName(ABC):  '''

from abc import ABC, abstractmethod   
class Car(ABC):   
    def mileage(self):   
        pass  
  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")          
# Driver code   
t= Tesla ()   
t.mileage()   

'''We use the @abstractmethod decorator to define an abstract method or if we don't provide the definition to the method, 
it automatically becomes the abstract method. '''

#Q)If abstract classes do no have any body then why are they required
'''Imagine an abstract class as a recipe template. 
It defines the required ingredients (methods and attributes) but doesn't provide the specific steps (implementation) 
for every recipe. Subclasses (specific recipes) inherit from the template, implementing the steps (providing their own code for the methods) 
while using the common ingredients defined in the abstract class. 
This ensures all recipes follow the same basic structure and have the necessary ingredients, 
but allows for customization in the preparation process.'''

#We can have both abstract and non-abstract method in an abstract class
#We cannot have abstract methods in normal class