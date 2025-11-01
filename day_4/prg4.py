class TooHot(Exception):
    def display(self):
        print("Too Hot")
class TooCold(Exception):
    def display(self):
        print("Too Cold")
try:
    t = int(input("Enter the temperature: "))
    if t > 40:
        raise TooHot()
    elif t < 20:
        raise TooCold()
    else:
        print("Temperature is:", t)
except TooHot as e:
    e.display()
except TooCold as e:
    e.display()