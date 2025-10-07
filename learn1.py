# This is a comment — ignored by Python

# Basic printing
print("Hello, Python!")  # Output: Hello, Python!

# Variables
name = "Samruddhi"
age = 21
is_student = True
height = 5.4

# Printing multiple things
print("Name:", name, "| Age:", age, "| Student:", is_student)

# You can also format strings
print(f"My name is {name}, I am {age} years old.")

print(type(name))
print(type(age))
print(type(is_student))
print(type(height))

# 💪 Mini Challenge

# Try writing a short script:

# Create variables for your name, age, and favorite_stock.

# Print a sentence using all three values in a formatted string like:

# My name is <name>, I am <age> years old, and my favorite stock is <stock>.

nameNew = "Samruddhi"
ageNew = 21
favourite_stock="Reliance"
print(f"My name is {nameNew}, I am {ageNew} years old and my favourite stock is {favourite_stock}")

# 🔹 1. Numbers (int, float)
age = 21          # int (integer)
height = 5.6      # float (decimal)

sum_value = age + 4
product = age * 2
div = height / 2
print(sum_value, product, div)


# 🔹 2. Strings (str) Strings are immutable (can’t be changed in place).
name = "Samruddhi" 
print(name.upper())     # SAMRUDDHI
print(name.lower())     # samruddhi
print(len(name))        # 9
print(name[0])          # First character: S
print(name[0:3])        # First 3 characters: Sam
print(name[4:])         # From 5th character to end: uddhi
print(name[-3:])        # Last 3 characters: dhi
print(name[::2])        # Every 2nd character: Smudi
print(name[::-1])       # Reverse: ihddurmaS
print(name.replace("Samruddhi", "Sam")) # Replace: Sam
print(name.split(" "))  # Split into list: ['Samruddhi']
print(name.join(["Sam", "ruddhi"])) # Join with: SamSamruddhiruddhi


# 🔹 3. Booleans (bool)
is_logged_in = True
has_premium = False
print(is_logged_in and has_premium)  # False
print(is_logged_in or has_premium)   # True


# 🔹 4. Lists (list)
# Lists are ordered, mutable, and can hold multiple types.

stocks = ["TCS", "Infosys", "Reliance"]
stocks.append("HDFC")        # Add
print(stocks)
stocks.remove("TCS")         # Remove
print(stocks)
print(stocks[0])             # Access element
print(len(stocks))           # Length

# 🔹 5. Tuples (tuple)
# Tuples are ordered but immutable (cannot be changed).

location = ("Mumbai", "India")
print(location[0])   # Mumbai

# 🔹 6. Dictionaries (dict)
# Key–value pairs — very useful for APIs and MongoDB documents.

user = {
    "name": "Samruddhi",
    "age": 21,
    "favourite_stock": "Reliance"
}

print(user["name"])        # Access value
user["city"] = "Mumbai"    # Add key
print(user)

# 🔹 7. Sets (set)
# Unordered collection of unique items (no duplicates).

unique_stocks = {"TCS", "Infosys", "Reliance", "TCS"}
print(unique_stocks)   # {'Reliance', 'Infosys', 'TCS'}



# 💪 Mini Challenge

# Create a dictionary called stock_info:

# {
#   "symbol": "TCS",
#   "price": 3650,
#   "change_percent": 1.5
# }


# Then:

# Add a new key "volume" with value 1500000

# Print this message using f-string:

# TCS is trading at ₹3650 with 1.5% change and volume 1500000

stock_info={
    "symbol": "TCS",
    "price": 3650,
    "change_percent": 1.5
}

stock_info["volume"] = 1500000
print(stock_info)
print(f"TCS is trading at {stock_info['price']} with {stock_info['change_percent']} change and volume {stock_info['volume']}")


# 💪 Mini Challenge

# Try this:

# Create a tuple called coordinates = (19.0760, 72.8777) (Mumbai’s lat-long).

# Create a set called visited_cities = {"Mumbai", "Pune", "Delhi"}.

# Try adding "Mumbai" again and print the set.

# Notice what happens — why?
# These is the list 
coordinates = (19.0760, 72.8777)
visited_cities = ["Mumbai", "Pune", "Delhi"]
visited_cities.append("Mumbai")
print(visited_cities)
# ['Mumbai', 'Pune', 'Delhi', 'Mumbai']

# These is the set
visited_cities = {"Mumbai", "Pune", "Delhi"}
visited_cities.add("Mumbai")
print(visited_cities)
# {'Mumbai', 'Pune', 'Delhi'}


# Create a list of stocks with duplicates
stocks = ["TCS", "Infosys", "TCS", "HDFC", "Infosys"]
print(stocks)
# ['TCS', 'Infosys', 'TCS', 'HDFC', 'Infosys']

# Convert it to a set to remove duplicates
unique_stocks = set(stocks)
print(unique_stocks)
# {'HDFC', 'Infosys', 'TCS'}
# Print both the list and the set
