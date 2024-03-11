C does not allow you to count the length of an array like Python.
A Primary Key field contains unique values that cannot be replicated elsewhere in the table. This avoids potential confusion between tables with similarities in data.
  
NoSQL databases are a type of database that store data in a variety of different formats.

You are utilizing CRUD operations on the data in your database. Which of the following actions can you perform on the data using these operations? Check all that apply
Create data
Read data
Update data
Delete data

#Iteration One
before = input("before: ")
print ("After: ", end="")
print (before.upper())

#Iteration Two
before = input("before: ")
after = before.upper()
print(f"After: {after}")

#Iteration Three
before = input("before: ")
print(f"After: {before.upper()}")

def calculator():
    x = int(input("Enter A: "))
    y = int(input("Enter B: "))
    print (x + y)

calculator()

exlist = [1, 3, 5, 7, 9, 11, 70]
average = sum(exlist) / len(exlist)

print(average)
print(f"Average: {average}")

def main():
    woof(4)

for _ in range(4):
    print("Eenis")

def define():
    for _ in range(2):
        print("Define")

define()

for _ in range (1):
    define()

def woof(n):
    for _ in range(n):
        print("Woof!")

main()

def calculator():
    x = int(input("Enter A: "))
    y = int(input("Enter B: "))
    print (x + y)

calculator()

exlist = [1, 3, 5, 7, 9, 11, 70]
average = sum(exlist) / len(exlist)

print(average)
print(f"Average: {average}")

scores = []
for i in range(3):
    score = int(input("Score "))
    scores.append(score)

average2 = sum(scores) / len(scores)
print(f"Average: {average2}")

names = ["Steve", "Bob", "Dave"]
name = input("Name: ")
#for n in names:
#    if name == n:
#        print("Found")
#       break
if name in names: #Uses linear search
    print("Found") 
else:
    print ("Not Found")

#A LIST of DICTIONARIES
people = [
    {"Name": "Bob", "Number": "012"},
    {"Name": "Dave", "Number": "456"},
    {"Name": "Steve", "Number": "890"},
]

name = input("Name: ")

for person in people:
    if person["Name"] == name:
        number = person["Number"]
        print(f"Found: {number}")
        break
else:
    print("Not Found")

people2 = {
    "Bobby": "Mild",
    "Bibby": "Spicy",
    "Blobby": "Hot",
}

name2 = input("Name2: ")

if name2 in people2:
    number = people2[name2]
    print(f"Found: {number}")
else:
    print("Not Found")

import sys #To make python worse
if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

print(f"hello, {sys.argv[1]}")
sys.exit(0)
