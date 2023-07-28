class Animal:
    def __init__(self, name, species, habitat):
        self.name = name
        self.species = species
        self.habitat = habitat

    def make_sound(self):
        print("Generic animal sound")

class Lion(Animal):
    def __init__(self, name, species, habitat, mane_color):
        super().__init__(name, species, habitat)
        self.mane_color = mane_color

    def make_sound(self):
        print()
        print(f"{self.name} the {self.species} from {self.habitat} says: Roar!")
        print(f"{self.name}'s mane color is {self.mane_color}.")
        print()

class Frog(Animal):
    def __init__(self, name, species, habitat, jump_height):
        super().__init__(name, species, habitat)
        self.jump_height = jump_height

    def make_sound(self):
        print(f"{self.name} the {self.species} from {self.habitat} says: Croak!")
        print(f"{self.name} can jump up to {self.jump_height} meters high.")
        print()

class Snake(Animal):
    def __init__(self, name, species, habitat, length):
        super().__init__(name, species, habitat)
        self.length = length

    def make_sound(self):
        print(f"{self.name} the {self.species} from {self.habitat} says: Hiss!")
        print(f"{self.name}'s length is {self.length} meters.")
        print()

def animal_in_zoo_sound(animal_obj):
    animal_obj.make_sound()

lion = Lion("Labert", "Lion", "Savanna", "golden")
frog = Frog("Tyco", "Frog", "Pond", 1.5)
snake = Snake("Python", "Snake", "Jungle", 3.2)

animal_in_zoo_sound(lion)
animal_in_zoo_sound(frog)
animal_in_zoo_sound(snake)
