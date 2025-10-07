# 🧩 Step 1: What is a Class?

# Think of a class as a blueprint or design.

# Example:
# Imagine we’re building a “User” system (like in your login API).
# All users share the same structure — they all have a name, email, password, etc.
# So we create a User class to describe what a user looks like.

# 🧩 Step 2: What is an Object?

# An object is a real thing made from that blueprint.

# Example:

# The “class” is the blueprint for a car.

# The “object” is your specific car (like a red Honda).

# In code:

# class Car:
#     pass  # means 'nothing yet'


# Now make an object:

# my_car = Car()


# Here:

# Car → class (blueprint)

# my_car → object (real car built from blueprint)

# 🧩 Step 3: Adding Data (Attributes)

# We can make our class store data about each object.

# We do this using a special method called __init__
# (pronounced “dunder init” — double underscore init).

# It runs automatically when you create an object.

class Car:
    def __init__(self, brand, color):
        self.brand = brand      # store brand inside the object
        self.color = color      # store color inside the object


# Now create an object:
car1 = Car("Honda", "Red")
car2 = Car("BMW", "Black")
print(car1.brand)   # Honda
print(car2.color)   # Black


# 🧩 Step 4: Adding Behavior (Methods)

# Functions inside a class are called methods.
# They let your object do something.

# Example:

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show_info(self):
        print(f"This is a {self.color} {self.brand}.")


# Now create and call:

my_car = Car("Honda", "Red")
my_car.show_info()


# ✅ Output:

# This is a Red Honda.

# 🧩 Step 5: What is self?

# The word self just means “this particular object”.

# When you write:

# my_car.show_info()


# Internally Python does this:

# Car.show_info(my_car)


# So self = my_car.
# It’s how each object knows its own data.

# Example:

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")


# Now:

dog1 = Dog("Tommy")
dog2 = Dog("Sheru")

dog1.bark()  # Tommy says Woof!
dog2.bark()  # Sheru says Woof!


# Each dog remembers its own name because of self.

# 🧩 Step 6: Why We Need OOP in Backend

# When you’ll build your Login API, you’ll use classes like:

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def check_password(self, entered_password):
        return self.password == entered_password


# Now, when a user logs in:

user = User("samruddhi@gmail.com", "1234")
if user.check_password("1234"):
    print("Login successful!")
else:
    print("Wrong password!")


# ✅ Output:

# Login successful!


# This is exactly how real systems like FastAPI structure their logic —
# everything revolves around classes: Users, Orders, Products, Payments, etc.

# 💪 Mini Challenge (Super Easy)

# Make a class User:

# It should store name and email using __init__

# It should have a method show_user() that prints:

# User: Samruddhi | Email: samruddhi@gmail.com


# Create 2 users and call the method for both.

class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email


    def show_user(self):
        print(f"User: {self.name} | Email: {self.email}")

user1 = User("Samruddhi", "samruddhi@gmail.com")
user2 = User("Akshay", "akshay@gmail.com")
user1.show_user()
user2.show_user()

# ✅ Output:
# User: Samruddhi | Email: samruddhi@gmail.com
# User: Akshay | Email: akshay@gmail.com