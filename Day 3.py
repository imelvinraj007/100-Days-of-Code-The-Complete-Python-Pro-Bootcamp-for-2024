# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm? "))
# bill = 0
# if height >= 120:
#     print("you can ride rollercoaster")
#     age = int(input("What is your age?"))
#     if age <= 12:
#      print("You have to pay $5")
#      bill = 5
#     elif age <= 18:
#        print("You have to pay $7")
#        bill = 7
#     else:
#      print("You have to pay $12")
#      bill = 12
    
#     want_photo = input("Do you want the photo ? Y or N?")
#     if want_photo == "Y":
#        bill += 3

#     print(f"Your total bill is {bill}")

# else:
#     print("Sorry you have to grow taller before you ride")



# year = int(input())

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not leap year")

# print("Thank you for choosing Python Pizza Deliveries!")
# size = input() # What size pizza do you want? S, M, or L
# add_pepperoni = input() # Do you want pepperoni? Y or N
# extra_cheese = input() # Do you want extra cheese? Y or N
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}")


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇
dic = input("left or right?")
if dic == "left":
    act = input("swim or wait")
    if act == "wait":
        door = input("Which door?")
        if door == "red":
            print("Burned by fire.Game Over.")
        elif door == "blue":
            print("Eaten by beasts.Game Over.")
        elif door == "yellow":
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.Game Over.")
else:
    print("Fall into a hole.Game Over")
