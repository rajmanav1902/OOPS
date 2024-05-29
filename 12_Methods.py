#Methods
'''In python there are mainly 3 types of methods:
1.Instance/Regular methods
2.Static methods
3.Class methods'''

#Instance methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create Person objects
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

person1.greet()  # Output: Hello, my name is Alice and I am 30 years old.
person2.greet()  # Output: Hello, my name is Bob and I am 25 years old.

#Static methods
'''Static methods are not bound to either the class or its objects. 
They behave like regular functions defined within the class but can access class attributes if needed.
You use the @staticmethod decorator to define a static method.
Static methods are typically utility functions that don't rely on object data or modify class state. 
They might be used for helper functions or calculations related to the class concept but not specific to object instances.'''
class MathHelper:
  @staticmethod
  def add(x, y):
    return x + y

result = MathHelper.add(5, 3)  # Call like a regular function
print(result)  # Output: 8

#Class methods
'''Class methods receive the class itself as the first argument (usually named cls). 
This allows them to operate on the class itself, such as creating or modifying class attributes 
or alternative constructors for object initialization.'''
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  @classmethod
  def from_coordinates(cls, x, y):
    return cls(x, y)  # Return a new Point instance

point = Point.from_coordinates(3, 4)
print(point.x, point.y)  # Output: 3 4

'''Key Points:

Use instance methods for object-specific behavior.
Use static methods for utility functions that don't rely on object data or class state.
Use class methods for operations on the class itself or alternative constructors.'''
