class Animal:
    def __init__(self,color, types, HP):
        self.color = color
        self.types = types
        self.HP = HP
    
    def hunt(self, time):
        self.HP = self.HP - time*5
        return self.HP
    
    def eat(self, time):
        self.HP = self.HP + time*10
        return self.HP

class Dog(Animal):
    def __init__(self,color, types, HP):
        super().__init__(color, types, HP)
    
    def barking(self):
        print('汪汪汪')

class BullDog(Dog):
    def __init__(self,color, types, HP):
        super().__init__(color, types, HP)
    
    def barking(self):
        print('吼吼吼')
    
john = Animal('yellow','bulldog',12000)    
peter = Dog('yellow','bulldog',12000)
chris = BullDog('yellow','bulldog',12000)