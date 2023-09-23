#Syntax Errors, tend to be misspelling or typo. Minimal impact, most IDE's highlight it.
#Exception Errors, known errors that need to be handled. E.g Trying to divide by 0.

def divide_by(a,b):
    return a / b

print(divide_by(10,2))

#Using the exception as e, we can print the specific error.
try:
    print(divide_by(10,0)) #division by 0 is not possible.
except Exception as e:
    print("Something went wrong:", e)   
except ZeroDivisionError as e:
    print("This will give a specific Error", e)

print(divide_by(10,2))

# Starter code
items = [1,2,3,4,5]
try:
    item = items[6]
    print(item)
except Exception as e:
    print("Item does not exist in the list:", e)

#### ####

loyalty_customer = True
total_bill = 124
if loyalty_customer and total_bill > 100:
    #give 20% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 20
elif total_bill > 100:
    #give 10% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 10
else:
    #sorry no discount, 5% service charge applied.
    print('Sorry, no discount ...')
print('Total Bill: ', float(total_bill))

#2
current = False
if current:
    current = False
    print('Turning light off')
if not current:
    current = True
    print('Turning light on')
    
#3
current = False
if current:
    current = False
    print('Turning light off')
else: 
    current = True
    print('Turning light on')

#4
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']
for dessert in favorites:
    print('One of my favorite desserts is', dessert)

#5
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']
count = 0

while count < len(favorites):
    print('One of my favorite desserts is', favorites[count]);
    count += 1

num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

