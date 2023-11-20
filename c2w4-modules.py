#Modules
#A module can be any .py file. You cannot call other file types, such as txt or xml.

import numpy #Will only work after numpy has been installed. Will work if numpy is a built in module.

import sys #Importing sys to specify a path
sys.path.insert(1, r'C:\windows\examplefolder')#1 = First indexed location, r = Used when passing a location as an argument.
#The sys.path list now has a new path to check for modules

#Once the folder locationhas been established, a file within can be called.
import examplefile #The file name in the location is examplefile.py
print (examplefile.names) #Within this file, is a variable called names.

#Importing Modules via import.py
import math #math is a built in module
print("Testing the import of the math module") #Most inbuilt modules do not say if they are loaded

root = math.sqrt(9)
print(root)

from math import sqrt #Import a single component instead of the entire math package.

root = sqrt(9) #The 'math.' part needs to be removed for this to work.
print(root)

import math as m #Alias, rename packages within a program

cosine = m.cos(0)
print (cosine)

from math import factorial as f #Import a specific function and give it an alias.

factorial_10 = f(10)
print(factorial_10)

from math import factorial, log10, sqrt # You can import multiple functions at the same time.
from math import * # This will import all of the functions of math

# If you import math, you can use math functions with a dot notation. math. sqrt, for example.
# If you from math import *, all math names are available without the dot notation.

from math import nonsense #Will throw an error as this function does not exist in math.

# Namespaces and Scopes
# Namespaces - Maps names to objects
# Scope is the textial region of a python program with an accessable namespace.
# The are 4 scopes in Python: Local, Enclosed, Global and Built-In.
# 1. Local: A variable inside a function is local.
# 2. Global: A function outside of a variable is global.
# Working with global variables in not common in large software projects.
# Access Modifiers, Concurrency and Memory Allocation are better handled as local variables.

# Nonlocal Function - Used within nested functions, nonlocal is used to access and modify variables from the nearest enclosing scope that is not global.
def a(): #3) Once called, assign 'B' to the local variable.
    animal = "B" #Local value. Commenting out this line will throw an error. I dont entirely understand why.
    def b(): #4) Then declare the inner function b().
        nonlocal animal
        animal = "C" #7)Once inside b(), you declare the nonlocal animal is now 'C'.
        print ("Inside nest function: "+animal)

    print ("Before calling function: "+animal) #5)Print the local value, which is 'B'.
    b() #6) Call the b() function, run this before printing the next line.
    print ("Print after nested function: "+animal) #8)Print the current animal, which is still C.

animal = "A" #1) Global variable is A.
a() #2) Call the a() function
print("Global Animal: " +animal) #Will print A, as the global variable was not affected by the local changes.

#Reload()
#Assumption - sample.py external file with "Hello, world" written into it.
import Example # The .py extension not required.
import Example # Multiple import statements will not work, it will only load once.

import importlib # importlib contains the reload function.
import Example

importlib.reload(Example) # By using the reload function, we can run the external script as many times as we like.
importlib.reload(Example)
importlib.reload(Example)
importlib.reload(Example)

#filechanges.py
import importlib
import Example

def changes():
    try:
        importlib.reload(Example)
        Example.print_changes()
    except:
        pass

for i in range(5):
    changes()
    input("Hit enter to reload.. ")

#Example.py
import os

def print_changes():
    contents = os.listdir(r'C:\Users\Tovey\Dropbox\GitHub') # The r is so the interpreter reads the path as raw string.
    print("Current  Directory Contents: ")
    print(contents)

#Differences between Modules, libraries and packages.
# Modules: A module is a single file.
# Packages: A package is a collection of modules.
# Libraries: A library is a collection of packages.

# By default, pip is installed with Python. However to check if python is installed, you can run the following commands, either in the console or the IDE terminal:
py -m ensurepip --upgrade # windows
python -m ensurepip --upgrade # mac

# To install a third party packages such as 'requests', run the following:
py -m pip install requests # Windows
python3 -m pip install requests # mac
