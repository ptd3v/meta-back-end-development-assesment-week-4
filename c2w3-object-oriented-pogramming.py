#Object Orientated Programming (OOP)
#Popular examples of OOP: Python, Java, C++.
#OOP is highly modular, making code easy to understand.

#Classes, objects and methods.
#Class - Logical code block, contains attributes(variables) and behaviours(functions).
#Objects - An instance of a class, 
#Methods - Functions defined with a class that determine the behaviour of an instance.

#4 Concepts of OOP
#Inheritance - Creating a new class from an old one. E.g A parent class, can have a child class which is a copy.
#Polymorphism - A single function can act differently depending on te object. E.g str+str concatenates, 1+2 adds.
#Encapsulation - Prevents access to variables and methods by wrapping them in a class.
#Abstraction - Ability to hide implementation details for data security. E.g You can run functions, you don't need to know how they work.

#Python classes and instances
#Objects - Everything in Python is an object.
#Classes - Creating a class, creates a new type of object.
#Instances - An instance, is a copy of a class.
#Variables - 
#Methods - 
#Attributes - Variables declared in a class
#Behaviours - Methods in a class

#Class and Instance Example
class MyClass: #Class object
  a = 5
  print("Hello")
    def hello():
      print("Hello World!") #Method
  pass #pass is a placeholder, it executes nothing.

newinstance  = MyClass() #Instance object
print(MyClass.a) #Reference a class object
print(newinstance.a) #Reference an instance object

#Execise: Define a Class
class House: #Class
    num_rooms = 5 #Attribute
    bathrooms = 2 #Attribute
    def cost_evaluation(self):
        print(self.num_rooms) #Function
        pass #Stock Holder Text

house = House() #Instance of a class, an object.
print(house.num_rooms)
print(House.num_rooms)

house.num_rooms = 7 #Updating the 'house' instance, NOT the class 'House'.
print(house.num_rooms)
print(House.num_rooms)

House.num_rooms = 7 #Updating the Class, this will also update the instance (object).
print(house.num_rooms)
print(House.num_rooms)

#Instantiate a custom Object
#Referencing the same variables and methods in different instances can produce different outcomes.
#Meaning that the code is reusable.

class Recipe():
    def __new__(cls) -> Self: #cls = placeholder for passing class as a new argument
        pass #The __new__ method creates an empty object
    def __init__(self) -> None: #Takes the object created by the _new_ method and initialises it.
        pass #The Self text is a placeholder for self-reference by the instance object.

#Two special methods in python.
#First is 'New' method which creates and returns a new empty object.
#Second is __init__, similar to a constructor in other languages.

class Recipe(): #Use the state of an object to my advantage.
    def __init__(self, dish, items, time) -> None:
        self.dish = dish #Three new variables
        self.items = items #To hold the recipe ingredients
        self.time = time

    def contents(self): #Produce a string out of this information
        print("The " + self.dish + "has " + str(self.items) + "and takes " + str(self.time) + "min to prepare")

pizza = Recipe("Pizza", ["cheese", "bread", "tomato"], 45)
pasta = Recipe("Pasta", ["penne", "sause"], 65)

# Instantiate a custom Object Exercise
class MyFirstClass():
    print("Who wrote this?")
    index = "Author-Book"

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book)

whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War")

print(pasta.items) #Prints onlt the items
print(pizza.items)

print(pizza.contents()) #Prints the entire statement.

#Class = Cake Recipe/ House Blueprint
#Object = Object is a cake made using that recipe/ House

# Instance Methods
class PaySlips: #Class
  def __init__(self, name, payment, amount) -> None:
    #self.variable = variable
    self.name = name
    self.payment = payment
    self.amount = amount

  def pay(self): #Function 1
    self.payment = "yes"

  def status(self): #Function 2, contains an If/Else Statement
    if self.payment == "yes":
      return self.name + " is paid " + str(self.amount)
    else:
      return self.name + " is not paid"

#Two Instances
nathan = PaySlips("Nathan", "No", 1000)
jerry = PaySlips("Jerry", "Yes", 2000)

print(nathan.status(), "\n" ,  jerry.status())

jerry.pay() #Call the function pay()

print("New Payments Added: ", "\n", nathan.status(), "\n" ,  jerry.status())

#Multiple Inheritance
# Example of multiple inheritance
class A:
   a = 1
  
class B:
   b = 2  
  
class C(A, B):
   pass

c = C()
print(c.a, c.b) # The output in 2 1.

#Multi-level inheritance
class A:
   a = 1

class B(A):
   a = 2

class C(B):
   pass

c = C()
print(c.a) # The output is 2 because C derives from the immediate super class of C, and that's B.
