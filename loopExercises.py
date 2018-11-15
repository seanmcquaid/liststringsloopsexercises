# # 1 to 10 

# for i in range(1, 11):
#     print i

# # user prompted range

# x = int(raw_input("what number would you like to start from? "))
# y = int(raw_input("what number would you like to end on? "))

# print "Start from: %i " % x
# print "End on: %i " % y 

# for i in range(x,y):
#     print i

# # odd numbers

# for i in range(1,11):
#     if (i % 2 == 0):
#         pass
#     else:
#         print i

# # print a square

# size = 5

# for i in range(size):
#     print("*" * size)

# # print a square based on a user prompt size 

# size = int(raw_input("How big is the square? "))

# for i in range(size):
#     print("*" * size)

# print a hollow square with user specified dimensions

# Print a Triangle
# Print a triangle consisting of * characters like this:

#    *
#   ***
#  *****
# *******

p = int(raw_input("How big is your triangle? "))
p = p + 1

for i in range (1, p, 2):
    print ("-" * p) + (i * "*")
    p -= 1