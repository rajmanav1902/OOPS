'''In other programming languages, there are static variables which have data common to all the object.
There is one copy of static variables which is shared by all the objects.'''

#In python, this concept is implemented using different approaches

#Class variable
'''While not technically static variables, class variables are declared inside a class but outside any methods. 
There's a single copy of the class variable shared by all instances of the class.'''
class Counter:
  # Class variable (shared by all instances)
  count = 0

  def __init__(self):
    Counter.count += 1  # Incrementing class variable in constructor

  def get_count(self):
    return Counter.count

# Creating instances doesn't affect the variable itself, but the value gets updated
counter1 = Counter()
counter2 = Counter()

print(counter1.get_count())  # Output: 2
print(counter2.get_count())  # Output: 2 (shared value)

#Modifying a class variable through one instance affects the value for all instances.

#Difference between class and instance variables?
'''
1.Each object has its own copy of isntance variables but there is only one copy of class variables which is shared 
by all objects
2. Any modifications made to isntance variables by an object will not affect the values in other object.This
 is not the case with class variables'''
class Counter:
  # Class variable
  count = 0

  def __init__(self, name):
    # Instance variable 
    self.name = name
    Counter.count += 1

  def get_info(self):
    # Access both class and instance variables
    return f"Object name: {self.name}, Total objects created: {Counter.count}"

# Create two Counter objects
counter1 = Counter("C1")
counter2 = Counter("C2")
print(counter1.get_info())  
print(counter2.get_info())  

# Accessing class variable directly 
print(f"Total count (class variable): {Counter.count}")

'''Note: we can access class variable by object but you shouldn't'''

#Difference between static and class variable
'''Think of a classroom. The class rules (like MAX_STUDENTS) are similar to a static variable 
(shared by all students). However, a whiteboard (acting as a class variable in Python) might be used for 
notes or examples that can be modified during class (with potential side effects for all students).'''

'''A class variable provides more flexibility in modifying it which can have negative impact'''
 

