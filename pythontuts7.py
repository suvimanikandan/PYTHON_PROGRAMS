
class student:

 def __init__(self,m1,m2):
    self.m1=m1
    self.m2=m2

 def sum(self, a,b,c):
     pass


def sum(self, a=None,b=None,c=None):
    s=0
    if a!=None and b!=None and c!=None:
        s=a+b+c
    elif a!=None and b!=None:
        s=a+b
    else:
        s=a

    return s


print(s.sum(3,5,9))