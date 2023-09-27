#Creating Files
#This will create a new document called 'newfile.txt'.
with open('newfile.txt', 'w') as file:
    file.writelines(["This is a newly created file", "\nThis is a second line to the file."])

with open('newfile.txt', 'a') as file:
    file.writelines(["\n\nAppended a new line", "\nAnd added a new, new row."])

#Adding exception handling to file creation
try:
    #Added sample/ to create an error.
    with open('sample/newfile.txt', 'a') as file:
        file.writelines(["\n\nAppended a new line", "\nAnd added a new, new row."])

except FileNotFoundError as e:
    print("File not found!", e)

#File Handling. File open options are: r/(read), r+/ (read + write), w/ (write), and a (append). Two possible outputs: text (default) or binary(rb, rb+, wb, ab).
#Basic file opening commands.
file = open('test.txt', mode = 'r')
data = file.readlines()
print(data)
file.close()

#With open is better at exception handling and will auto-close the file.
with open('test.txt', mode = 'r') as file:
    data = file.readlines()
    print(data)

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

#Solutions, Task 1 : IndexError
try:
    item = items[6]
    print(item)
except: 
    print("The index does not exist in the list.")

#Solutions, Task 2 : ZeroDivisionError
def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print(e, 'Something went wrong!')

ans = divide_by(10,0)
print(ans)

#Solutions, Task 3 : FileNotFoundError
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print("Unable to locate file")


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
