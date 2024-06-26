#Code reusability
'''In inheritance, the child class acquires the properties and can access all the data members and functions defined in the parent class. 
A child class can also provide its specific implementation to the functions of the parent class. '''

#Syntax
class Animal:  
    def speak(self):  
        print("Animal Speaking") 

#child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  

d = Dog()  
d.bark()  
d.speak()  

#Above is example of single inheritance

#Multi-level
class Animal:  
    def speak(self):  
        print("Animal Speaking")  
#The child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
#The child class Dogchild inherits another child class Dog  
class DogChild(Dog):  
    def eat(self):  
        print("Eating bread...")  
d = DogChild()  
d.bark()  
d.speak()  
d.eat()  


#Multiple inheritance
class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
d = Derived()  
print(d.Summation(10,20))  
print(d.Multiplication(10,20))  
print(d.Divide(10,20))

#issubclass(subclass,supclass):Returns True or False
#isinstance (obj, class):Returns True or False
