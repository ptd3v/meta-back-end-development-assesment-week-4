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

#Popular package examples:
import numpy as np #1) numpy
a = np.zeros(10)
print(a) # Creates an array with n number of 0's in it. For this example, 10 zeroes.

b = np.full((2,10), 0.7)
print(b) # creates a two-dimensional matrix of dimensions 2 x 10 consisting only of the values 0.7

c = np.linspace(0,25,7)
print(c) # Divides the values between 0 and 25 in 7 equal parts.

print(type(c))

[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] #The output
[[0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7]
 [0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7]] 
[ 0.          4.16666667  8.33333333 12.5        16.66666667 20.83333333  25.        ]
<class 'numpy.ndarray'> #All class types in numPy will be 'ndarray'. It it NumPy exclusive and a far more efficient lsit substitute.

----

import pandas as pd # 2) Pandas

a = pd.DataFrame({'Animals': ['Dog','Cat','Lion','Cow','Elephant'],
                    'Sounds':['Barks','Meow','Roars','Moo','Trumpet']})
print(a) #Prints the pandas dataframe
print(a.describe()) # The describe() function in pandas that will give the count, frequency, top values and frequency among other values.

b = pd.DataFrame({
    "Letters" : ['a', 'b', 'c', 'd', 'e', 'f'],
    "Numbers" : [12, 7, 9, 3, 5, 1]  })

print(b.sort_values(by="Numbers")) #A sorting function that will provide a sorted table leading to shuffling of the data entries in the table.

b = b.assign(new_values = b['Numbers']*3)
print(b) # The assign() function takes the values present inside the table, performs an operation on them and creates a new variable called new_values, that is then added to the table.

# 2) Output
    Animals   Sounds
0       Dog    Barks
1       Cat     Meow
2      Lion    Roars
3       Cow      Moo
4  Elephant  Trumpet

       Animals Sounds
count        5      5
unique       5      5
top        Dog  Barks
freq         1      1

  Letters  Numbers
5       f        1
3       d        3
4       e        5
1       b        7
2       c        9
0       a       12

  Letters  Numbers  new_values
0       a       12          36
1       b        7          21
2       c        9          27
3       d        3           9
4       e        5          15
5       f        1           3

----

#NLTK
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."

# Print statement 1
print(word_tokenize(text))
# Print statement 2
print(nltk.tokenize.sent_tokenize(text))

stopwords = stopwords.words("english")
new_text = []
for i in text.split():
    if i not in stopwords:
        new_text.append(i)

# Print statement 3
print(new_text)

# NLTK Output
['Lorem', 'Ipsum', 'is', 'simply', 'dummy', 'text', 'of', 'the', 'printing', 'and', 'typesetting', 'industry', '.', 'Lorem', 'Ipsum', 'has', 'been', 'the', 'industry', "'s", 'standard', 'dummy', 'text', 'ever', 'since', 'the', '1500s', ',', 'when', 'an', 'unknown', 'printer', 'took', 'a', 'galley', 'of', 'type', 'and', 'scrambled', 'it', 'to', 'make', 'a', 'type', 'specimen', 'book', '.']

['Lorem Ipsum is simply dummy text of the printing and typesetting industry.', "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."]

['Lorem', 'Ipsum', 'simply', 'dummy', 'text', 'printing', 'typesetting', 'industry.', 'Lorem', 'Ipsum', "industry's", 'standard', 'dummy', 'text', 'ever', 'since', '1500s,', 'unknown', 'printer', 'took', 'galley', 'type', 'scrambled', 'make', 'type', 'specimen', 'book.']

---- 

#Popular Data Science Modules: numPy, sciPy, Matplotlib, Skikit-Learn.
# NumPy: Numerical Python.
# Matplotlib: Used for Data Visualisation. 
# Skikit-Learn is used for predictive learning.
# Pandas: Python Data Analysis. Used for cleaning, analysing and manipulating data. Most common uses are: Reading CSV files and .json objects.

#Web Development:
# Djano and Flask are two of the most popular examples:
# Django: High level, fullstack* framework, encourages clean design and rapid development.
# *Full stack meaning it has everyting required on its own: Features and Libraries, Security, Templating and Support.
# Flask: Micro framework, simple and easy to use as a large library of addons.

#Testing - The main types of testing:
# Integration testing combines the unit tests and tests the flow of data from one component to another.
# In unit or component testing, the program tests specific individual components by isolating them.
# System testing is testing all the software. 
# Acceptance testing is when the stakeholders and a select few end-users are involved in acceptance testing.
