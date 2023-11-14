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
