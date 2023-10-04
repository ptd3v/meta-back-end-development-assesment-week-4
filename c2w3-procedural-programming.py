#Procedural Programming: Course 2/9. Week 3/5.
#Advantages: Easy to Learn/ Understand. Reusable.
#Disadvantages: Hard to maintain/ Extend. Exposed Data.

#Inefficient Code
a = 1
b = 2
sum = a + b
print(sum)

#Efficient Code
def sum(a, b):
  return a + b
print(sum(1,2))
print(sum(3,4))

#### ####

#Algorithms
def palindrome(str):
    startIndex = 0
    endIndex = len(str) - 1

    for x in str:
        if str[startIndex] != str[endIndex]:
            return False
    return True

print(palindrome('racecar'))

#Exercise: Make a cup of coffee

#Logical process:
#Ingredients required: Cup, Hot Water, Instant Coffee.
#Optional: Milk, Cream, Sugar.
#Output: Cup of Coffee
#Notes: Pseudocode describes the algorithmic flow and does not have instructions that may be confusing to read.

#Refactoring:
#A constant time algorithm means that the speed of an operation will always be the same. E.g Dictionaries accessing an element in an array by its index.
#A linear time algorithm means that the speed of an operation will decrease as the input increases. e.g Searching for a specific value in an unsorted list.
#Logarithmic Time: Grows with the size of the input data. E.g Binary search in a sorted list. Logarithmic time complexity is considered very efficient.

#Functional Programming
