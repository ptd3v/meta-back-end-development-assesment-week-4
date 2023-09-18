#Reuable Function Example, Adding Tax
#Unstructured Function
bill = 150.00
tax_rate = 15
total_tax = (bill * tax_rate) / 100.00
print ('Total Tax: ', total_tax)

#Structured Function
def calculate_bill (bill, tax_rate):
  return (bill * tax_rate) /100.00

#Note: Functions only run when they are called.
print ('Total Tax: ',calculate_bill(250,15))

#### ####

#Local and Global Variables
Built_in_var = 5
global_var= 10
def fn1 ():
  enclosed_var = 40
  def fn2():
    local_var = 20

#Reminder: Functions only run when they are called.
fn1()
print('Global Var: ', global_var,) #'Local Var: ', local_var, 'Enclosed Var: ', enclosed_var

#### ####

#Data Strcuture Types
#In-Built: List, Tuple, Dictionary, Set
#User-Defined: Stack, Tree, Graph, Queue, Linked List, HashMap 

#### ####

#Lists
list1 = [1, 2, 3, 4, 5]
list2 = ['A', 'B', 'C', 'D', 'E']
list3 = ['String', 1, 1.2, True]
list4 = [1, [2, 3, 4], 5, 6] #Nested List

print (list4[1]) #Print the value at index 1
print(*list4, sep = ", ")

list4.insert(4, 69) #Add the number 69, to position 4. Nice.
list4.insert(len(list4), 0) #Add 0 to the end of List4. Len is to calculate the total size, ensuring it adds to the end.
list4.extend([96, 97, 98])
list4.append(99)
print(*list4, sep = ", ")
list4.pop(0) #Remove the value at index 0
del list4[0] #Remove the new value at index 0
print(*list4, sep = ", ")

#Iterating through Lists
for x in list4:
    print('Value: ', x)

#Tuples
#Tuples
my_list = [2, True, 'String', 10.9] #Creates a list. Mutable.
my_tuple = (2, True, 'String', 10.9) #Creates a tuple. Immutable.
my_test = 2, True, 'String', 10.9 #Creates a tuple. Immutable.

print(my_tuple[1])
print(type(my_list))
print(type(my_tuple))
print(type(my_test))

print(my_tuple.count(True)) #Counts the occurances of the word 'string'.
print(my_tuple.index(10.9))
for x in my_tuple:
    print(x)

#my_tuple[0] = False #Will produce an error, tuples are immutable.

#Sets
set_a = {0, 1, 2, 3, 4, 5, 5} #Sets do not allow duplicate values.
set_a.add(5) #Methods are functions e.g Set, List, Tuple.
set_a.add(6)
set_a.remove(2)
set_a.add(2)
set_a.discard(5)
print(set_a)

set_b = {5, 6, 7, 8, 9, 10}
print(set_b)

print(set_a.union(set_b)) #Joins sets together, minus duplicates.
print(set_a | set_b)#.union simplified.
print(set_a.intersection(set_b)) #Prints only the common values.
print(set_a & set_b)#.intersection simplified.

print(set_a.difference(set_b))#Show all that's in A and not in B.
print(set_a - set_b)#.difference simplified.
print(set_a.symmetric_difference(set_b))#Show elements that are in set A and set B, but not both.
print(set_a ^ set_b)#.symmetric_difference simplified.

#print(set_a[0]) #Will throw an error because sets are not indexed.
