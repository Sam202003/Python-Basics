# 🧠 Lesson 6: Basic Algorithms (Sorting & Searching)

# 🔹 1. Sorting

# Sorting means rearranging items in order (ascending or descending).

# Python gives us built-in ways to do this easily.

# ✅ Example 1: Sort a List
prices = [560, 120, 450, 80, 340]
prices.sort()  # changes the list directly
print(prices)


# Output:

# [80, 120, 340, 450, 560]


# Descending order:

prices.sort(reverse=True)
print(prices)
# # [560, 450, 340, 120, 80]

# ✅ Example 2: Sort without changing original list

# Use sorted() instead of .sort()

prices = [560, 120, 450]
sorted_prices = sorted(prices)
print(prices)         # [560, 120, 450]
print(sorted_prices)  # [120, 450, 560]

# ✅ Example 3: Sort list of dictionaries (like API response)
stocks = [
    {"symbol": "TCS", "price": 3650},
    {"symbol": "Reliance", "price": 2500},
    {"symbol": "Infosys", "price": 1500}
]

sorted_stocks = sorted(stocks, key=lambda x: x["price"], reverse=True)
for s in sorted_stocks:
    print(s)


# Output:

# {'symbol': 'TCS', 'price': 3650}
# {'symbol': 'Reliance', 'price': 2500}
# {'symbol': 'Infosys', 'price': 1500}


# 💡 Here we used lambda (an inline function) — you’ll use this a lot when sorting data before sending API responses.

# 🔹 2. Searching

# Searching means finding whether an item exists in a list or not.

# ✅ Example 1: Simple Search
stocks = ["TCS", "Reliance", "Infosys"]

if "TCS" in stocks:
    print("Stock found!")
else:
    print("Stock not found.")


# Output:

# Stock found!

# ✅ Example 2: Loop-based Search
stocks = ["TCS", "Reliance", "Infosys"]
search = "HDFC"

found = False
for s in stocks:
    if s == search:
        found = True
        break

if found:
    print("Stock found!")
else:
    print("Stock not found.")

# ✅ Example 3: Searching in List of Dicts
stocks = [
    {"symbol": "TCS", "price": 3650},
    {"symbol": "Reliance", "price": 2500}
]

search = "TCS"

for s in stocks:
    if s["symbol"] == search:
        print(f"{search} found with price ₹{s['price']}")
        break

# 💡 Backend Relevance

# In APIs, these are extremely common patterns:

# Searching = MongoDB find_one()

# Sorting = MongoDB find().sort("price", -1)

# You’re already learning the logic you’ll apply directly in your Login and Stock APIs.

# 💪 Mini Challenge

# Make a list:

# stock_prices = [560, 120, 450, 80, 340]

# Sort it in descending order.

# Search if price 450 exists — print "Found" or "Not found".

# Try it using both direct (in) and loop method.

stock_prices = [560, 120, 450, 80, 340]
stock_prices.sort(reverse=True)
print(stock_prices)

if 450 in stock_prices:
    print("Found")
else:
    print("Not found")

for price in stock_prices:
    if price == 450:
        print("Found")
        break
    else:
        print("Not found")
        
        