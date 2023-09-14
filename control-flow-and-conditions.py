#Step 1: Unsorted list, sorted
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
num_list.sort()

#Testing: An enumerate function is used to provide the index of current iteration of a for loop.
num_index = enumerate(num_list)
print(list(num_index))

print (num_list)

for num in num_list:
    print(num)

count = 0

for i in num_list:
#Step 2: Print Under 45
  if i > 45:
    print("Over 45")
#Step 3: Print Over 45
  else:
    print("Under 45")

#Step 4: Enumerate Function
for x,num in enumerate(num_list):
#Step 5 and 6: Count +=1
  count += 1
  if num == 36:
    print('Number found at ', x)
    #Step 8: Break when found
    break
#Step 7: Print Count Value
print(count)

if 36 in num_list:
    index = num_list.index(36)
    print('Number found at', index + 1)
