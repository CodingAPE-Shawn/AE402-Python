class Animal:
    def __init__(self,types,HP,legs):
        self.types = types
        self.legs = legs
        self.HP = HP
    
    def run(self):
        self.HP -=30
        return self.HP
    
    def hunt(self):
        self.HP +=50
        return self.HP
    
#Dog = Animal("dog",4,100)
#print("dog hunt HP",Dog.hunt())

class Dog(Animal):
    def __init__(self,types,HP,legs=4):
        super().__init__(types,HP,legs=4)
    def getFrisbee(self):
        self.HP-=10
        print("搖尾巴")
        print("NEW HP:",self.HP)

    
    

    
    
    