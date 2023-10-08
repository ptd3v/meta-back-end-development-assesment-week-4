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
#Ingredients required: Cup, Hot Water, Instant Coffee. Optional: Milk, Cream, Sugar. Output: Cup of Coffee
#Notes: Pseudocode describes the algorithmic flow and does not have instructions that may be confusing to read.

#Refactoring:
#A constant time algorithm means that the speed of an operation will always be the same. E.g Dictionaries accessing an element in an array by its index.
#A linear time algorithm means that the speed of an operation will decrease as the input increases. e.g Searching for a specific value in an unsorted list.
#Logarithmic Time: Grows with the size of the input data. E.g Binary search in a sorted list. Logarithmic time complexity is considered very efficient.

#Functional Programming
#Pure functions are functions that always provide the same result, regardless of how many times it's run.
#Pure functions are used in functional programming to assure the integrity of data outside the scope of the pure function.

#Traditional Function, modified to be a Pure Function:
list = [0,1,2,3]
def append(item):
  return list.append(item)

append(4)
print(list)

#Recursion: Is a function that calls itself, similar to a for loop.
#Advantages: Easy to follow, problems broken down. Can be hard to follow, debug and can be memory efficient inefficient.
#Disasdvantages: 
def find_factoral(n):
    if n == 1:
      return 1
    else:
       return n * find_factoral(n - 1)
    
print(find_factoral(5))

#Recursion example: Towers of Hanoi
