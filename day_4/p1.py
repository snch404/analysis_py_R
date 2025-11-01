# def add(a,b):
#     return a+b
# def decor(add):
#     def inner_function(x,y):
#         if x < 0:
#             x = 0
#         if y < 0:
#             y = 0
#         return add(x,y)
#     return inner_function

# print(add(-60,60))
# add=decor(add)
# print(add(-60,60))

# def my_gen():
#     n = 1
#     yield n
#     n += 1
#     yield n
#     n += 1
#     yield n

# # calling a function
# a = my_gen()
# print(a)
# print(type(a))
# print(next(a))
# print(next(a))
# print(next(a))

branch=["CSE","AIML","ECE","IOT"]
for choice in branch:
    if(choice=="ECE"):
        print("Belong to ECE")
        break
else:
    print("Not from this branch")