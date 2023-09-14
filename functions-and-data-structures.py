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

