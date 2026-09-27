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

#phno/email
while True:           
    choice=int(input("Enter---1 to register with phno---or---2 to register with email---: "))
    if choice == 1:
        while True:
            num=int(input("Enter your PH.no: "))
            if len(str(num)) > 10 or len(str(num)) < 10:
                print("invalid input -- Enter valid PH.no")
            else:
                break 
        break
    elif choice == 2:
        email=input("Enter Your Email ID: ")
        break
    else:
        print("INVALID input -- Enter 1 or 2")

#print
print("Name =", name)
if choice == 1:
    print("PHno. =", num)
if choice == 2:
    print("EmailID =", email)


#menu card

menu = {
    "Pizza": 120,
    "Burger": 80,
    "Pasta": 100,
    "Sandwich": 60,
    "French Fries": 50,
    "Momos": 70,
    "Noodles": 90,
    "Biryani": 150,
    "Ice Cream": 60,
    "Cold Drink": 40
}

print("----------MENU----------")
for item, price in menu.items():
    print(f"{item:20} {price:.2f}₹")

        
    
