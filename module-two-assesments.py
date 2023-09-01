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
    
# 3
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
