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

food = []
price = []
total = 0 
ind = 0 
slno = 1

while True:
    khana = input("Enter food choice from menu (q to quit ): ")
    for item in menu:                                                               #AI    #case of input and key didnt match sowanted a solution to match the case 
        if khana.lower() == item.lower():                                           #AI    #thats why i used AI to fix this problem and added these 4 lines of code
            khana = item                                                            #AI
            break                                                                   #AI
    if khana.lower() == "q":
        print("THANK you for VISITING US")
        break
    elif khana not in list(menu):                                           
        print("We Dont serve that food pls choose from MENU")
    else:
        food.append(khana)
        pyce= menu[khana]
        price.append(pyce)
        total += pyce
print()
print("--------------YOUR CART--------------")
print()
print(f"Name = {name}")
if choice == 1:
    print("PHno = ", num)
if choice == 2:
    print("Email = ", email)
print()

for foods in food:
    print(f"{slno}) {foods:20}{price[ind]:.2f}₹")
    ind += 1 
    slno +=1
        
print()
print(f"YOUR TOTAL           = {total:.2f}₹")
print()
print("-----THANK YOU for VISITING US :)-----")

