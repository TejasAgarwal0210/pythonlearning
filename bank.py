#defining the class

class Bank:
    amount = 0 

    @classmethod
    def deposit(cls):
        depamt = int(input("Enter the amount to deposit: "))
        Bank.amount += depamt
        print(f"{depamt} has been deposited in your account.")
        print(f"Your current balance is: {Bank.amount}")

    @classmethod
    def credit(cls):
        credamt = int(input("Enter the amount to withdraw"))

        if (Bank.amount-credamt) >= 0:
            Bank.amount -= credamt
            print(f"{credamt} has been credited from your account") 
            print(f"Your current balance is: {Bank.amount}")

        else:
            print("INSUFFICIENT FUNDS IN YOUR ACC, your balance is", Bank.amount)
            print("TRANSACTION FAILED")

#signup
#name
while True:
    name=input("Enter your name (not more than 14char): ")
    if len(name) > 14:
        print("invalid input -- pls enter <= 14 char")
    elif not name.replace(" ", "").isalpha():
        print("invalid input -- pls enter only alphabets")
    else:
        break

#phno
while True:           
    phno = int(input("Enter your ph no to link your bank account: "))
    if len(str(phno)) != 10:
        print("INVALID PHNO")
    else:
        break

print(F"Your NAME: {name}")
print(f"Your account number: {phno}")

#chosing what to do

choicedict = { 1 : "DEPOSIT MONEY", 
                2 : "CREDIT MONEY",
                3 : "TOTAL BALANCE", 
                4 : "ACC STATUS",
                5 : "QUIT BANK"}

print("----------CHOSE WHAT YOU WANT TO DO------------")

for x,y in choicedict.items():
    print(f"{x:5} {y:}")

while True:
    choice = int(input("Enter your Choice: "))
    if choice not in choicedict:
        print("INVALID CHOICE, pls enter a valid choice")
    else:        
        if choice == 1:
            Bank.deposit()

        elif choice == 2:
            Bank.credit()

        elif choice == 3:
            print(f"Your total balance is {Bank.amount}")

        elif choice == 4:
            print(f"Your Name = {name}")
            print(f"Your Account Number = {phno}")

        elif choice == 5:
            print(f"Thank You {name.upper} for choosing our bank.")
            break




