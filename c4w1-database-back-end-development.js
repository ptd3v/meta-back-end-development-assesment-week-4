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

SQL requires few coding skills to use. 
SQL can run on any hardware or operating system.
SQL works with all relational databases.
SQL covers all areas of database management and administration.

import csv
with open("example.csv", "r") as file:
  varread = csv.DictReader(file) 
    #DictReader reads the columb titles, #Reader does not
      #next(reader) #start at line [1] to ignore header
  for row in reader:
    favourite = row["language"] #With DictReader, the data is now a dictionary, not a list. 
    print(favourite)

#Assuming a .csv file that contains which letters a survey find best. The options are a, b or c.
a, b, c = 0, 0 , 0

  for row in reader:
    favourite = ["language"] # Results stored in the language columb.
      if favourite == "a":
        a += 1
      elif favourite == "b":
        b += 1
      elif favourite == "c":
        c += 1

print(f"A: {a}")
print(f"B: {b}")
print(f"C: {c}")

counter = {} #Empty Dictionary

for row in reader:
  favorate = row["language"]
  if favourite in sorted(counts):
    counts[favorite] += 1
  else:
    counts[favorite] = 1

#SQL schema example
.schema tablename
  CREAT TABLE example
  show_id INTEGER NOT NULL,
  title TEXT NOT NULL,
  FOREIGN KEY(show_id) REFERENCES shows(id)
  FOREIGN KEY(person_id) REFERENCES people(id)

#IMDB Three DB not merged, searching via a middle DB.
SELECT title FROM shows WHERE id IN
  (SELECT show_id FROM stars WHERE person_id =
    (SELECT is FROM people WHERE name = 'Steve Carell'));

#Joining three DB for the same search.
SELECT title FROM shows
  JOIN stars ON shows.id = stars.show_id
    JOIN people ON stars.person_id = people_id
     WHERE name = 'Steve Carell';

#More optimal method, matching through Primary and foreign keys
SELECT title FROM shows, stars, people
  WHERE shows.id = stars.show_id
  AND people.id = stars.person_id
  AND name = 'Steve Carell'

CURL = Connect to URL
curl -I https://www.harvard.edu

nginx
Apache

You can populate a table with data using Data Manipulation Language.


Data in a table is organized into rows and columns.
A table relates to other tables in the same database.
In a database that holds multiple tables, the tables are referred to as “relations” because they“relate” to one another.
A table is sometimes also known as an “entity.”
A table also often referred to as an “entity” in a more logical sense.
