# Write a program that randomly generates a number. 
# Raise a user-defined exception if the number is below 0.5.
class Less(Exception):
    def display(self):
        print("Number is below 0.5")
import random
try:
    n=random.random()
    print(n)
    if(n<0.5):
        raise Less()
except Less as e:
    e.display()
else:
    print("Number is above 0.5")