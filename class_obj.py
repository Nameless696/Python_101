
class HumanBeing():
    greet = "Welcome Human"#class variable
    def __init__(self,name):
        self.name=name#instance variable
        
    #instance method
    def print_name(self):
        print(f'Name is {self.name},{self.greet}')
        
    #class method
    @classmethod #decorators
    def greeting(cls):
        print(f'{cls.greet}')
        
    #static method
    @staticmethod #decorators
    def do_something():
        hello="welcome to static method"
        print(hello)

#instance method call
bibidh_object = HumanBeing("bibidh")
bibidh_object.print_name()
bibidh_object.greeting()
bibidh_object.do_something()
print()

#instance method call
reya_object = HumanBeing("reya")
reya_object.print_name()
print()


#class method call
human_being_greeting = HumanBeing.greeting()

#static method call
human_being_do_some_thing = HumanBeing.do_something()




