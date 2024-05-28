'''Encapsulation in Python is a fundamental concept in object-oriented programming (OOP) that focuses on bundling 
data (attributes) and methods (functions) that operate on that data together within a single unit, a class'''

'''Attributes (Data):

Within the class, you define attributes to represent the data the class holds. 
These attributes can be public, private, or protected (although access modifiers aren't strictly enforced like in some other languages).

Public Attributes: These attributes are accessible directly from outside the class using dot notation (e.g., object.attribute).

Private Attributes: By convention, attributes prefixed with double underscores (__) are considered private. While they can still be accessed from outside the class, it's generally discouraged as it weakens encapsulation.

Protected Attributes: While Python doesn't have a built-in protected keyword, you can use a single leading underscore (_) to indicate that the attribute is intended for internal use within the class and its subclasses.'''

class Book:

  def __init__(self, title, author, year):
    # Public attributes
    self.title = title
    self.author = author
    self.year = year

  # Public method to modify title (controlled access)
  def set_title(self, new_title):
    self.title = new_title

  # Private method for internal calculations (not meant for external use)
  def __calculate_age(self):
    from datetime import date  # Import for illustration
    current_year = date.today().year
    return current_year - self.year

  # Public method to get book age using private method (controlled access)
  def get_age(self):
    return self. __calculate_age()  # Call private method internally

# Create a Book object
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)

# Access public attributes (not recommended)
print(book1.title)  # Output: The Hitchhiker's Guide to the Galaxy

# Modify title using public method (recommended)
book1.set_title("A Hitchhiker's Guide to the Galaxy")
print(book1.title)  # Output: A Hitchhiker's Guide to the Galaxy

# Get book age using public method (controlled access)
print(f"Book age: {book1.get_age()} years")  # Output: Book age: 46 years (assuming current year is 2024)
