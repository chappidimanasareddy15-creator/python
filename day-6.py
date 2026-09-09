# ==========================================
# CLOTHES BUSINESS - MODULES & PACKAGES
# ==========================================

# ------------------------------------------
# 1. IMPORTING A MODULE
# ------------------------------------------

import math

price = 1200
quantity = 5

total = price * quantity

print("Total Clothes Price:", total)
print("Square Root of Price:", math.sqrt(price))
#------------------------------------------
#output
#------------------------------------------
Total Clothes Price: 6000
Square Root of Price: 34.64101615137755

# ------------------------------------------
# 2. IMPORTING SPECIFIC FUNCTION
# ------------------------------------------

from math import ceil, floor

discount = 1250.75

print("Rounded Up Discount:", ceil(discount))
print("Rounded Down Discount:", floor(discount))
#------------------------------------------
#output
#------------------------------------------
Rounded Up Discount: 1251
Rounded Down Discount: 1250
# ------------------------------------------
# 3. IMPORT MODULE WITH AN ALIAS
# ------------------------------------------

import random as r

# Generate a random discount
random_discount = r.randint(5, 30)

print("Random Discount:", random_discount, "%")
#------------------------------------------
#output
#------------------------------------------
Random Discount: 5 %
# ------------------------------------------
# 4. IMPORT MULTIPLE FUNCTIONS
# ------------------------------------------

from datetime import datetime, date

current_date = date.today()
current_time = datetime.now()

print("Today's Date:", current_date)
print("Current Date & Time:", current_time)
#------------------------------------------
#output
#------------------------------------------
Today's Date: 2026-09-08
Current Date & Time: 2026-09-08 17:11:12.136754
# ------------------------------------------
# 5. USING MATH MODULE
# ------------------------------------------

cloth_price = 999
discount_percent = 10

discount_amount = cloth_price * discount_percent / 100
final_price = cloth_price - discount_amount

print("\n===== MATH MODULE =====")
print("Cloth Price:", cloth_price)
print("Discount:", discount_amount)
print("Final Price:", final_price)

print("Rounded Final Price:", math.ceil(final_price))
#------------------------------------------
#output
#------------------------------------------
Cloth Price: 999
Discount: 99.9
Final Price: 899.1
Rounded Final Price: 900
# ------------------------------------------
# 6. USING RANDOM MODULE
# ------------------------------------------

clothes = ["Shirt", "Jeans", "Frock", "Saree", "Jacket"]

selected_cloth = random_cloth = r.choice(clothes)

print("\n===== RANDOM MODULE =====")
print("Randomly Selected Cloth:", selected_cloth)

# Random number of clothes sold
sold_quantity = r.randint(1, 10)

print("Random Sold Quantity:", sold_quantity)
#------------------------------------------
#output
#------------------------------------------
Randomly Selected Cloth: Saree
Random Sold Quantity: 10
# ------------------------------------------
# 7. USING DATETIME MODULE
# ------------------------------------------

today = date.today()

print("\n===== DATETIME MODULE =====")
print("Business Date:", today)

# Create a sale date
sale_date = datetime(2026, 9, 8, 10, 30)

print("Sale Date & Time:", sale_date)
#------------------------------------------
#output
#------------------------------------------
Business Date: 2026-09-08
Sale Date & Time: 2026-09-08 10:30:00

# ------------------------------------------
# 8. CREATING YOUR OWN MODULE
# ------------------------------------------

# Suppose we create a file called:
# clothes_utils.py
#
# Inside clothes_utils.py:
#
# def calculate_discount(price, discount):
#     return price * discount / 100
#
# def calculate_profit(cost, selling):
#     return selling - cost


# Then we can import our own module:
#
# import clothes_utils
#
# discount = clothes_utils.calculate_discount(2000, 10)
# profit = clothes_utils.calculate_profit(1500, 2000)
#
# print(discount)
# print(profit)
#------------------------------------------
#output
#------------------------------------------
Cost Price: 1500
Selling Price: 2200
Discount: 15 %

# ------------------------------------------
# 9. USING OWN MODULE WITH ALIAS
# ------------------------------------------

# Example:
#
# import clothes_utils as cu
#
# discount = cu.calculate_discount(3000, 20)
# profit = cu.calculate_profit(2000, 3000)
#
# print("Discount:", discount)
# print("Profit:", profit)
#------------------------------------------
#output
#------------------------------------------
Discount: 15 %
Profit: 370.0
# ------------------------------------------
# 10. PACKAGE
# ------------------------------------------

# A package is a folder containing Python modules.
#
# Example structure:
#
# clothes_business/
#     __init__.py
#     discount.py
#     profit.py
#
# discount.py:
#     def calculate_discount(price, discount):
#         return price * discount / 100
#
# profit.py:
#     def calculate_profit(cost, selling):
#         return selling - cost
#
# We can import them using:
#
# from clothes_business import discount
# from clothes_business import profit
#
# discount_amount = discount.calculate_discount(2500, 15)
# profit_amount = profit.calculate_profit(1800, 2500)
#------------------------------------------
#output
#------------------------------------------
Discount: 15 %
Discount Amount: 330.0
Final Price: 1870.0
Profit: 370.0
# ------------------------------------------
# 11. REAL CLOTHES BUSINESS EXAMPLE
# ------------------------------------------

cost_price = 1500
selling_price = 2200
discount_percent = 15

discount_amount = selling_price * discount_percent / 100
final_price = selling_price - discount_amount
profit = final_price - cost_price

print("\n===== CLOTHES BUSINESS =====")
print("Cost Price:", cost_price)
print("Selling Price:", selling_price)
print("Discount:", discount_percent, "%")
print("Discount Amount:", discount_amount)
print("Final Price:", final_price)
print("Profit:", profit)
#------------------------------------------
#output
#------------------------------------------
Cost Price: 1500
Selling Price: 2200
Discount: 15 %
Discount Amount: 330.0
Final Price: 1870.0
Profit: 370.0
# ------------------------------------------
# 12. RANDOM CUSTOMER OFFER
# ------------------------------------------

offers = [5, 10, 15, 20, 25]

customer_offer = r.choice(offers)

offer_amount = selling_price * customer_offer / 100
offer_price = selling_price - offer_amount

print("\n===== CUSTOMER OFFER =====")
print("Customer Discount:", customer_offer, "%")
print("Offer Amount:", offer_amount)
print("Offer Price:", offer_price)
#------------------------------------------
#output
#------------------------------------------
Customer Discount: 5 %
Offer Amount: 110.0
Offer Price: 2090.0
# ------------------------------------------
# FINAL SUMMARY
# ------------------------------------------

print("\n==============================")
print("     CLOTHES BUSINESS")
print("==============================")
print("Business Date:", today)
print("Product:", "Frock")
print("Selling Price:", selling_price)
print("Final Price:", final_price)
print("Profit:", profit)
print("Customer Offer:", customer_offer, "%")
#------------------------------------------------
#output
#-------------------------------------------------
Business Date: 2026-09-08
Product: Frock
Selling Price: 2200
Final Price: 1870.0
Profit: 370.0
Customer Offer: 5 %
