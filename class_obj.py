
class HumanBeing():
    greet = "Welcome Humans"
    def __init__(self,name):
        self.name=name
        
    def greeting(self):
        print(f'{self.greet}, {self.name}')

bibidh_object = HumanBeing("bibidh")
reya_object = HumanBeing("reya")
bibidh_object.greeting()
print()
reya_object.greeting()
