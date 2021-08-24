class car:
    wheels = 5

    def __init__(self):
        self.mil =  10
        self.com = "BMW"



c1 = car()
c2= car()

c2.mil = 8
car.wheels = 10
print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)