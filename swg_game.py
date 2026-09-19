import random

gdict = { "s" : 1, "w" : 2, "g" : 3 }

while True:
    computerchoice = random.choice(list(gdict.keys()))
    perinp = input("Enter your choice (s for snake, w for water, g for gun, or q to quit): ")
    if perinp == "q":
        print("Exiting the game. Goodbye!")
        break
    else:
        while perinp not in gdict:
            print("Invalid input. Please enter 's', 'w', or 'g'.")
            perinp = input("Enter your choice (s for snake, w for water, g for gun): ")

        print("Your choice is: ", perinp)
        print("Computer choice is: ", computerchoice)


        if perinp == computerchoice:
            print("It's a tie!")
        elif (perinp == "s" and computerchoice == "w") or (perinp == "w" and computerchoice == "g") or (perinp == "g" and computerchoice == "s"):
            print("You win!")
        else:
            print("Computer wins!")
