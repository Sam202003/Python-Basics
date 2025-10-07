# 🧠 Lesson 3: Conditionals & Loops
# 🔹 1. Conditionals — Decision Making in Code

# Python uses indentation to define what code runs inside a condition
is_logged_in = True
user_role = "admin"

if is_logged_in:
    print("Welcome back!")

    if user_role == "admin":
        print("Access granted to dashboard.")
    else:
        print("Limited access.")
else:
    print("Please log in first.")
# Welcome back!
# Access granted to dashboard.

age = 21
if age < 18:
    print("Minor")
elif age == 18:
    print("Just became adult!")
else:
    print("Adult")

age=24;
if age < 21:
    print("You are not an adult")
elif age==21:
    print("your an adult")
else:
    print("you are a senior citizen")

# 🔹 2. Loops — Repeating Tasks
# 🔸 for loop

# Iterates through a sequence (list, tuple, dict, set, or range):

stocks = ["TCS", "Infosys", "Reliance", "HDFC"]
for stock in stocks:
    print(stock);


# With range():

for i in range(3):
    print(i)

# 🔸 while loop

# Runs until a condition becomes False:

count = 1
while count <= 3:
    print("Attempt:", count)
    count += 1


# ⚠️ Always make sure to increment or break — otherwise it loops forever.    

# 🔸 break and continue
for num in range(1, 6):
    if num == 3:
        continue     # skip 3
    if num == 5:
        break        # stop loop
    print(num)


# Output → 1 2 4

# 💪 Mini Challenge

# Write a small program:

# Make a list of stock prices: [120, 340, 560, 80, 450]

# Print only the prices greater than 200

# Also count how many such stocks exist

# Expected Output:

# Price: 340
# Price: 560
# Price: 450
# Total stocks above 200: 3

stock_prices = [120, 340, 560, 80, 450]
count = 0
for prices in stock_prices:
    if prices > 200:
        print(f"Price: {prices}")
        count += 1
print(f"Total stocks above 200: {count}")

# Price: 340
# Price: 560
# Price: 450
# Total stocks above 200: 5


# 💪 Mini Challenge (Realistic One)

# Write a program that:

# Takes a list of users = [21, 17, 25, 16, 30] (ages)

# Prints "Allowed" if age >= 18, otherwise "Not Allowed"

# Finally prints total allowed users count.

users = [21, 17, 25, 16, 30]
count =0;
for age in users : 
    if(age>=18):
        print("Allowed")
        count+=1
    else:
        print("Not Allowed")
print(f"Total allowed users: {count}")

# Allowed
# Not Allowed
# Allowed