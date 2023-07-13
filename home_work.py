import random

computer_score = 0
user_score = 0

rounds = int(input("Enter the number of rounds you want to play: "))

for round in range (1, rounds + 1):
    print(round,"ROUNDS")
    
    user_guess = int(input("Choose a number between 1 to 6: "))
    print("You choose:", user_guess)
    
    computer_guess = random.randint(0,6)
    print("Computer choose:", computer_guess)
    
    if user_guess > computer_guess:
        user_score += 1 
        print("You win this round.")
        
    elif computer_guess > user_guess:
        computer_score += 1
        print("The computer wins this round.")
        
    else:
         print("ITS A TIE!!")
         user_score += 1
         computer_score += 1
        
    print("user_score: ", user_score)
    print("computer_score: ", computer_score)
    print()
    
print("AND THE FINAL SCORES ARE:")
print("YOUR SCORE:", user_score)
print("COMPUTERS SCORE:", computer_score)

if user_guess > computer_guess:
    print("CONGRATS YOU WON!!")
elif computer_guess > user_guess:
    print("OHHH THE COMPUTER WON BETTER LUCK NEXT TIME!!")
else:
    print("ITS A TIE...TRY AGAIN!!")

