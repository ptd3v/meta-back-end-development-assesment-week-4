#Modules
#A module can be any .py file. You cannot call other file types, such as txt or xml.

import numpy #Will only work after numpy has been installed. Will work if numpy is a built in module.

import sys #Importing sys to specify a path
sys.path.insert(1, r'C:\windows\examplefolder')#1 = First indexed location, r = Used when passing a location as an argument.
#The sys.path list now has a new path to check for modules

#Once the folder locationhas been established, a file within can be called.
import examplefile #The file name in the location is examplefile.py
print (examplefile.names) #Within this file, is a variable called names.

