class computer:

    def __init__(self):
       self.name="swetha"
       self.age=30


    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

    def update(self):
        self.age =19

c1 = computer()
c1.age=30


c2 = computer()
c2.age=29
c2.update()

if c1.compare(c2):
    print("they are same")
else:
    print("they are  diffeerent")


print(c1.name)
print(c2.age)

