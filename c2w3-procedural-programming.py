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
