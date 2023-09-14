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
