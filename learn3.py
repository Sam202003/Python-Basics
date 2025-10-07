# Lesson 4: Functions — Reusable Logic Blocks
# When building APIs, you’ll repeatedly do things like:
# Validate input
# Hash passwords
# Connect to databases
# Return formatted responses
# Instead of rewriting logic each time, we wrap it into functions.

# 🔹 Basic Syntax
def greet_user(name):
  print(f"Hello, {name}! Welcome back.")
greet_user("Samruddhi")

def greet_new_user(new_user):
    print(f"Hello, {new_user}! Welcome to the platform.")
# Calling the function:
greet_new_user("Samruddhi")
# ✅ Output:
# Hello, Samruddhi! Welcome back.
# Hello, Samruddhi! Welcome to the platform.


# 🔹 Functions with Return Values
# If you want a function to give something back (not just print):

def add(a, b):
    return a + b

result = add(5, 10)
print(result)  # Output: 15

def sub(a, b):
    return a-b  
result = sub(10, 5)
print(result)  # Output: 5


# 🔹 Default Parameters
def greet(name="Guest"):
    print(f"Welcome, {name}!")

greet()          # Welcome, Guest!
greet("Riya")    # Welcome, Riya!

def greetSam(name="Sam"):
    print(f"Welcome, {name}!")

greetSam()
greetSam("Samruddhi")

# 🔹 Multiple Return Values (Tuple)
def get_user():
    name = "Samruddhi"
    age = 21
    return name, age

user_name, user_age = get_user()
print(user_name, user_age)

def get_user_details():
    name = "Akshay"
    age = 22
    return name, age 
user_name, user_age = get_user_details()
print(user_name, user_age)

# 💡 Real Backend Example

# When we build the Login API later:

# def verify_password(plain_password, hashed_password):
#     return bcrypt.checkpw(plain_password.encode(), hashed_password)


# Here the function returns True/False based on password validity — this is exactly how functions power backend logic.


# 💪 Mini Challenge

# Write a function:

# def filter_stocks_above(prices, limit):
    # return a list of prices above limit


# Example:

# filter_stocks_above([120, 340, 560, 80, 450], 200)


# should return:

# [340, 560, 450]

def filter_stocks_above(prices,limit):
    return [price for price in prices if price > limit]

print(filter_stocks_above([120, 340, 560, 80, 450], 200))

# [340, 560, 450]