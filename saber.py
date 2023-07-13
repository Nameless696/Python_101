animal = input("Enter the type of animal you wanna identify(omnivorous,carnivorous,herbivorous): ")

if animal == "omnivorous" or animal == "Both": 
   print("Omnivorous eat both Meat and vegetables!")
   
elif animal == "carnivorous" or animal == "meat only":
    print("Carnivorous eat only Meat!")
    
elif animal == "herbivorous" or animal == "vegetable only":
    print("Herbivorous eat only Vegetables!")
    
else:
    print("Unknown animal type")

