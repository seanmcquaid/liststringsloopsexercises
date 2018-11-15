# 1 to 10 

for i in range(1, 11):
    print i

# user prompted range

x = int(raw_input("what number would you like to start from? "))
y = int(raw_input("what number would you like to end on? "))

print "Start from: %i " % x
print "End on: %i " % y 

for i in range(x,y):
    print i

# odd numbers

for i in range(1,11):
    if (i % 2 == 0):
        pass
    else:
        print i

# print a square

size = 5

for i in range(size):
    print("*" * size)

# print a square based on a user prompt size 

size = int(raw_input("How big is the square? "))

for i in range(size):
    print("*" * size)