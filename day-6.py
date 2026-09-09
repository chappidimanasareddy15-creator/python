# ==========================================
# MODULES & PACKAGES - MOBILE SHOP
# ==========================================

# Importing built-in modules
import math
import random
import datetime


# ------------------------------------------
# 1. MATH MODULE
# ------------------------------------------

mobile_price = 25999

# ceil() - rounds up
print("Rounded Up Price:", math.ceil(mobile_price / 1000))

# floor() - rounds down
print("Rounded Down Price:", math.floor(mobile_price / 1000))

# sqrt() - square root
print("Square Root:", math.sqrt(256))
#------------------------------------------------
#output
#------------------------------------------------
Rounded Up Price: 26
Rounded Down Price: 25
Square Root: 16.0

# ------------------------------------------
# 2. RANDOM MODULE
# ------------------------------------------

mobile_brands = ["Samsung", "Apple", "OnePlus", "Vivo", "Oppo"]

# Select a random brand
random_brand = random.choice(mobile_brands)

print("Random Mobile Brand:", random_brand)

# Generate random discount
discount = random.randint(5, 20)

print("Random Discount:", discount, "%")
#------------------------------------------------
#output
#------------------------------------------------
Random Mobile Brand: Vivo
Random Discount: 6 %
# ------------------------------------------
# 3. DATETIME MODULE
# ------------------------------------------

today = datetime.datetime.now()

print("Current Date and Time:", today)

# Get only date
print("Today's Date:", today.date())

# Get year
print("Year:", today.year)

# Get month
print("Month:", today.month)
#------------------------------------------------
#output
#------------------------------------------------
Current Date and Time: 2026-09-09 12:43:40.198177
Today's Date: 2026-09-09
Year: 2026
Month: 9
Square Root using Alias: 25.0
# ------------------------------------------
# 4. CREATING YOUR OWN MODULE
# ------------------------------------------

# Suppose we have another file called mobile.py

# mobile.py
#
# def calculate_profit(cost, selling):
#     return selling - cost
#
# def calculate_discount(price, discount):
#     return price * discount / 100


# To import your own module:
#
# import mobile
#
# profit = mobile.calculate_profit(20000, 25000)
# discount_amount = mobile.calculate_discount(30000, 10)
#------------------------------------------------
#output
#------------------------------------------------
Mobile Profit: 5000
Discount Amount: 3000.0
# ------------------------------------------
# 5. IMPORT SPECIFIC FUNCTION
# ------------------------------------------

# Example:
#
# from mobile import calculate_profit
#
# profit = calculate_profit(20000, 25000)
# print("Profit:", profit)
#------------------------------------------------
#output
#------------------------------------------------
Mobile Profit: 5000
# ------------------------------------------
# 6. MODULE ALIAS
# ------------------------------------------

import math as m

print("Square Root using Alias:", m.sqrt(625))
#------------------------------------------------
#output
#------------------------------------------------

# ------------------------------------------
# 7. RANDOM MOBILE SALE
# ------------------------------------------

price = 30000

discount = random.randint(5, 20)

discount_amount = price * discount / 100

final_price = price - discount_amount

print("\n===== MOBILE SALE =====")
print("Original Price:", price)
print("Discount:", discount, "%")
print("Discount Amount:", discount_amount)
print("Final Price:", final_price)
#------------------------------------------------
#output
#------------------------------------------------
Original Price: 30000
Discount: 19 %
Discount Amount: 5700.0
Final Price: 24300.0

# ------------------------------------------
# 8. MOBILE SHOP DATE
# ------------------------------------------

sale_date = datetime.datetime.now()

print("\n===== SALE DETAILS =====")
print("Mobile:", random.choice(mobile_brands))
print("Sale Date:", sale_date.date())
print("Sale Time:", sale_date.time())
#------------------------------------------------
#output
#------------------------------------------------
Mobile: Apple
Sale Date: 2026-09-09
Sale Time: 12:43:40.212931
