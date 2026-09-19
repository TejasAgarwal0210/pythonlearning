import random 

ndict = {1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9 ,10}         # else ndict = range(1, 11) 
computerchoice = random.choice(list(ndict))

def perinp():
    guess = int(input("Enter your guess (a number between 1 and 10): "))
    return guess

while True: 
    guess = perinp()
    if guess not in ndict:
        print("Invalid input. Please enter a number between 1 and 10.")
    else:       
        if guess == computerchoice:
            print("Congratulations! You guessed the correct number:", computerchoice)
            break

        elif guess < computerchoice:
            print("Your guess is too low.")
        elif guess > computerchoice:
            print("Your guess is too high.")


        
    
