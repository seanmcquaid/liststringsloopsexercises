numbers = [-3,0,2,23,54,32,10]

#largest number
print max(numbers)

#smallest number
print min(numbers)

# even numbers
for num in numbers:
    if (num % 2 == 0):
        print num

# positive numbers 

for num in numbers:
    if (num > 0 ):
        print num

# append positive numbers to new list

positive_numbers = []

for num in numbers:
    if (num > 0):
        positive_numbers.append(num)

print positive_numbers

# multiply a list

product = []

for num in numbers:
    product.append(num * 5)

print product