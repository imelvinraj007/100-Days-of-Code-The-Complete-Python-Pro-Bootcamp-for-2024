
#print("Hello"[4])
#print(123+456)

# print("Please enter your number:")
# received_data = input()
# first_digit = int(received_data[0])
# second_digit = int(received_data[1])
# sum = str(first_digit + second_digit)
# print("your total is: " + sum)

# num_char = len(input("What is your name?"))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")

# weight = input()
# height = input()
# new_height = float(height)
# new_weight = int(weight)
# bmi = (new_weight / (new_height ** 2))
# new_bmi = int(bmi)
# print(new_bmi)

# print(8//3)

# print("Please enter your age:")
# age = input()
# years = 90 - int(age)
# months = (12 * int(years))
# weeks = (90 * int(years))
# days = (365 * int(years))

# print(f"You have {days} days, {weeks} weeks, {months} months, and {years} years ")

print("Welcome to the tip calculator.")
amount = (input("What was the total bill? $" ))
tip = input("What percentage tip would ypu like to give? 10, 12, or 15? " )
split = input("How many people to split the bill? ")
n_amount = float(amount)
n_split = float(split)
n_tip = float(tip)
bill_tip = (n_tip / 100) * n_amount + n_amount
cal = bill_tip / n_split
cal = round(cal ,2)
cal = "{:.2f}".format(cal)
print(f"Each person should pay: ${cal}")

