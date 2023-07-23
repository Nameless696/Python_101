class Mammal:
    def __init__(self, legs, eyes, name):
        self.legs = legs 
        self.eyes = eyes
        self.name = name
        
class HumanBeing(Mammal):
    def __init__(self, brain_power, legs, eyes, name):
        self.brain_power = brain_power
        super().__init__(legs, eyes, name)
    def print_details(self):
        print(f'Name is: {self.name}, Eyes: {self.eyes},Legs: {self.legs},IQ: {self.brain_power}')
        
class Cow(Mammal):
    def __init__(self, tail, legs, eyes, name):
        self.tail = tail
        super().__init__(legs, eyes, name)
    def print_details(self):
        print(f'Name is: {self.name},tail: {self.tail}, Eyes: {self.eyes},Legs: {self.legs}')
    

bibidh_object = HumanBeing("100","2","2","Bibidh")
bibidh_object.print_details()

cow_obj = Cow("1","4","2","Cow bekky")
cow_obj.print_details()