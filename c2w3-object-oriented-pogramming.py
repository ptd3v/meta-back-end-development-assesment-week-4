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
