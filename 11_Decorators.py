#Decorators
'''In Python, decorators are a powerful and versatile design pattern that allows you to modify 
the behavior of functions or classes without permanently altering their source code. 
They achieve this by adding functionality before or after the original function execution.'''

'''How Decorators Work:

Defining a Decorator:

A decorator is itself a function that takes another function as its argument.
This argument, often referred to as the wrapped function, is the function whose behavior you want to modify.
Inner Function (Wrapper):

Inside the decorator function, you typically define an inner function (often called a wrapper function).
This wrapper function can perform actions before, after, or both before and after the execution of the wrapped function.
Returning the Wrapper:

The decorator function usually returns the wrapper function. This returned function is then assigned to a variable or used to decorate another function.
Decoration Syntax:

The @ symbol is used for decoration syntax. You place the decorator function name above the function you want to decorate.'''
def timer(func):
  """Decorator that times the execution of a function."""
  import time

  def wrapper(*args, **kwargs):
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Function '{func.__name__}' took {elapsed_time:.4f} seconds to execute.")
    return result
  return wrapper

@timer
def my_function(n):
  """Calculates the factorial of a number."""
  factorial = 1
  for i in range(2, n + 1):
    factorial *= i
  return factorial

# Call the decorated function
result = my_function(5)
print(result)  # Output: 120

#@property
'''The @property decorator in Python is used to create properties. 
Properties are a special kind of method that act like attributes but provide more control over accessing and potentially modifying the underlying data. '''
class Circle:
  def __init__(self, radius):
    self._radius = radius  # Private attribute (using underscore prefix)

  @property
  def radius(self):
    return self._radius

  @radius.setter
  def radius(self, new_radius):
    if new_radius < 0:
      raise ValueError("Radius cannot be negative")
    self._radius = new_radius

  @property #Read only property
  def area(self):
    return 3.14 * self._radius * self._radius  # Computed property

circle = Circle(5)
print(circle.radius)  # Output: 5 (using the getter)
circle.radius = 10  # Using the setter (validation applied)
print(circle.area)  # Output: 78.5 (using the computed property)

#You can optionally define a setter method using @property.setter to control how the attribute's value is set.

