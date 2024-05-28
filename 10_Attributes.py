#Attributes
'''In Python, attributes are essentially variables associated with classes or objects. 
Variables inside a class are called attributes'''

#Class attributes
class Animal:
  # Class attribute (shared by all Animal objects)
  num_animals = 0

  def __init__(self, name):
    self.name = name
    Animal.num_animals += 1  # Increment class attribute in constructor

# Create animal objects
animal1 = Animal("Lion")
animal2 = Animal("Elephant")

print(animal1.num_animals)  # Output: 2 (shared class attribute)
print(Animal.num_animals)  # Output: 2 (accessing class attribute directly)

#Instance attribute
class Dog:
  def __init__(self, name, breed):
    self.name = name  # Instance attribute for dog's name
    self.breed = breed  # Instance attribute for dog's breed

# Create dog objects with unique attributes
dog1 = Dog("Buddy", "Labrador")
dog2 = Dog("Luna", "Golden Retriever")

print(dog1.name)  # Output: Buddy
print(dog2.breed)  # Output: Golden Retriever


