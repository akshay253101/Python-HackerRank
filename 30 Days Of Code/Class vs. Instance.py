class Person:
    def __init__(self,initialage):
        self.age = initialage
    def amIOld(self):
        if 0<=self.age < 13:
            print("You are young.")
        elif 13<=self.age<18:
            print("You are a teenager.")
        elif self.age>=18:
            print("You are old.")
        elif self.age<0:
            self.age = 0;
            print("Age is not valid, setting age to 0.")
            print("You are young.")
    def yearPasses(self):
        self.age = self.age+1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")