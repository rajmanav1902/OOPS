'''Polymorphism is a fundamental concept in object-oriented programming (OOP) 
that allows objects of different classes to respond to the same method call in different ways.'''

#1.Duck Typing:In Python, objects are like the ducks in the pond. They can belong to different classes, but what matters is their functionality.
def greet(animal):
  # Duck typing - as long as the object has a 'make_sound' method, it works
  animal.make_sound()

class Dog:
  def make_sound(self):
    print("Woof!")

class Cat:
  def make_sound(self):
    print("Meow!")

class Robot:  # Not an animal, but has a 'make_sound' method
  def make_sound(self):
    print("Beep boop!")

# Polymorphism in action
greet(Dog())  # Output: Woof!
greet(Cat())  # Output: Meow!
greet(Robot())  # Output: Beep boop! (Duck typing allows this)

#2.Operator overloading:
a=5
b=5
c=a+b
print("The sum"+"is",c)

#Method overloading
'''Python doesn't support traditional method overloading like some other languages. 
However, you can achieve similar functionality using alternative approaches:'''
#a.Default arguments
def greet(name="World"):  # Default argument for name
  print(f"Hello, {name}!")

greet()  # Output: Hello, World!
greet("Alice")  # Output: Hello, Alice!

#b.Variable length arguments
def calculate_average(*numbers):
  if not numbers:
    raise ValueError("Need at least one number for average")
  return sum(numbers) / len(numbers)

average1 = calculate_average(10, 20)  # Average of 2 numbers
average2 = calculate_average(30, 40, 50)  # Average of 3 numbers

print(average1)  # Output: 15.0
print(average2)  # Output: 40.0

#c.Keyword arguments
def create_user(name, email, age=None):  # Optional age argument
  return {"name": name, "email": email, "age": age}

user1 = create_user("Bob", "bob@email.com")
user2 = create_user("Alice", "alice@email.com", age=30)

print(user1)  # Output: {'name': 'Bob', 'email': 'bob@email.com'}
print(user2)  # Output: {'name': 'Alice', 'email': 'alice@email.com', 'age': 30}

#Method overriding(Run time polymorphism)
class Vehicle:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
  def start(self):
    print(f"The {self.make} {self.model} ({self.year}) is starting...")

class Car(Vehicle):
  def __init__(self, make, model, year, num_doors):
    super().__init__(make, model, year)  # Call parent class constructor
    self.num_doors = num_doors

  def start(self):
    super().start()  # Call parent class start() first (optional here)
    print(f"Turning on the car's engine and checking lights...")
    print(f"The {self.make} {self.model} ({self.year}) is ready to drive!")

def main():
  car = Car("Honda", "Civic", 2020, 4)
  car.start()

if __name__ == "__main__":
  main()

'''The line if __name__ == "__main__": main() is a common Python idiom used to conditionally execute code.
It's a concise way to ensure that a block of code only runs when the script is executed directly, 
not when it's imported as a module.'''

