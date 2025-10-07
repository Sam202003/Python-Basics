# 🧠 Lesson 5: Object-Oriented Programming (OOP)

# OOP helps you organize logic around real-world entities (like User, Stock, Order) instead of scattered functions.
# You’ll use this style in FastAPI for things like:

# User model

# AuthService (handles login, hashing, JWT)

# Database class (manages MongoDB connection)

# 🔹 1. Class & Object Basics

# A class is a blueprint.
# An object is an instance of that blueprint.

class Stock:
    # constructor (called automatically when object is created)
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

    # method (function inside a class)
    def show_info(self):
        print(f"{self.symbol} is trading at ₹{self.price}")


# Creating an object:

stock1 = Stock("TCS", 3650)
stock1.show_info()


# ✅ Output:

# TCS is trading at ₹3650