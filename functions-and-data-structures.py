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
