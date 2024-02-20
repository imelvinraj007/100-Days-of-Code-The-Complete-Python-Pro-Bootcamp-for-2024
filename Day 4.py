# import random
# random_num = random.randint(100,200)
# print(random_num)

# random_float = random.random() * 5
# print(random_float)

# love_score = random.randint(10,20)
# print(f"Your love score is {love_score}")

# states_of_america = ["D","P"]
# states_of_america[0] = "E"
# states_of_america.extend(["Meland","Nashland","Kevland"]) 
# print(states_of_america)

# import random
# dice = random.randint(0,1)

# if dice == 1:
#     print("Heads")
# else:
#     print("Tails")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game_images = [rock,paper,scissors]
user_input = int(input("What do you choose? Type 0 for rock, 1 for Paper, 2 for scissors.\n"))

if user_input >= 3 or user_input < 0:
    print("You typed an ivalid number loser")

else:
    print(game_images[user_input])
computer_input = random.randint(0,2)
print(f"Computer choose {computer_input}")
print(game_images[computer_input])

if user_input == 0 and computer_input == 2:
    print("User Wins")
elif computer_input == 0 and user_input == 2:
    print("Computer Wins")
    print("User Wins")
elif computer_input > user_input:
    print("Computer Wins")
elif computer_input == user_input:
    print("Draw")




