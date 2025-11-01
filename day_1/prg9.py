# Vivek went to a movie with his friends in a theatre and during break time he bought pizzas, puffs and cool drinks. Consider the following prices -> Rs.100/pizza -> Rs.20/puffs -> Rs.10/cool drink
#    Generate a bill for what Vivek has bought.
#    Sample Input 1:
#    -> Enter the no of pizzas bought: 10
#    -> Enter the no of puffs bought: 12
#    -> Enter the no of cool drinks bought: 5
#    Sample Output 1:
#    Bill Details
#    -> No of pizzas: 10
#    -> No of puffs: 12
#    -> No of cooldrinks: 5
#    -> Total price: 1290
#    ENJOY THE SHOW!!
pizzas = int(input("Enter the no of pizzas bought: "))
puffs = int(input("Enter the no of puffs bought: "))
cool_drinks = int(input("Enter the no of cool drinks bought: "))
total_price = (pizzas * 100) + (puffs * 20) + (cool_drinks * 10)
print("Bill Details")
print("-> No of pizzas:", pizzas)
print("-> No of puffs:", puffs)
print("-> No of cooldrinks:", cool_drinks)
print("-> Total price:", total_price)
print("ENJOY THE SHOW!!")