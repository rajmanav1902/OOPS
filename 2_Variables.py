'''For a class there are major 2 types of variables: Instance variable and Local variable'''

#Instance variables
'''Declared inside the class but outside any methods. 
Each object (instance) created from the class will have its own copy of these variables.'''
class Car:
  def __init__(self, color, model_year):
    # Instance variables
    self.color = color
    self.model_year = model_year

  def print_details(self):
    print(f"Color: {self.color}")
    print(f"Model year: {self.model_year}")

# Creating instances with different values
car1 = Car("Red", 2023)
car2 = Car("Blue", 2020)

car1.print_details()  
car2.print_details() 

#Local variables
'''Local variables are declared within a method of the class. 
They exist only during the execution of that specific method and are destroyed once the method finishes.'''
class Car:
  def __init__(self, color):  
    #Instance variable
    self.color = color

  def repaint(self, new_color):
    # Local variable
    original_color = self.color  # Storing instance variable in local variable
    self.color = new_color  # Modifying instance variable using local variable
    print(f"Car was repainted from {original_color} to {self.color}")

car1 = Car("Red")
car1.repaint("Blue") 

'''Note: It is not mandatory to initialize instance variables before use. They can have default values
It is compoulsory to initialize local variables before use. '''
