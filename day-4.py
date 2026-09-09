# BUSINESS DISCOUNT & PROFIT PROGRAM
# Lists, Tuples, Sets, Dictionaries, String Methods
# List & Dictionary Comprehensions

# --------------------------------------------------
# 1. LIST
# --------------------------------------------------

products = ["Laptop", "Mobile", "Headphones", "Keyboard"]

print("Products:", products)

# Accessing list
print("First product:", products[0])

# Adding item
products.append("Mouse")

# Removing item
products.remove("Keyboard")

# Updating item
products[1] = "Smartphone"

print("Updated products:", products)

# List slicing
print("First 3 products:", products[:3])
#-------------------------------------------------
#output
#--------------------------------------------------
Products: ['Laptop', 'Mobile', 'Headphones', 'Keyboard']
First product: Laptop
Updated products: ['Laptop', 'Smartphone', 'Headphones', 'Mouse']
First 3 products: ['Laptop', 'Smartphone', 'Headphones']



# --------------------------------------------------
# 2. TUPLE
# --------------------------------------------------

# Tuple is ordered and cannot be changed
business_details = ("BuyCart", "Tirupati", 2026)

print("\nBusiness Details:", business_details)
print("Business Name:", business_details[0])
print("Business Location:", business_details[1])

# Tuple unpacking
name, location, year = business_details
print("Name:", name)
print("Location:", location)
print("Year:", year)
#----------------------------------------------------
#output
#----------------------------------------------------
Business Details: ('BuyCart', 'Tirupati', 2026)
Business Name: BuyCart
Business Location: Tirupati
Name: BuyCart
Location: Tirupati
Year: 2026
# --------------------------------------------------
# 3. SET
# --------------------------------------------------

# Set stores unique values
categories = {"Electronics", "Mobiles", "Electronics", "Accessories"}

print("\nCategories:", categories)

# Add item
categories.add("Laptops")

# Remove item
categories.discard("Accessories")

print("Updated Categories:", categories)
#---------------------------------------------------
#output
#---------------------------------------------------
Categories: {'Electronics', 'Mobiles', 'Accessories'}
Updated Categories: {'Electronics', 'Mobiles', 'Laptops'}

Product: {'name': 'Laptop', 'cost_price': 40000, 'selling_price': 50000, 'discount': 10}
Product Name: Laptop
Cost Price: 40000
Updated Product: {'name': 'Laptop', 'cost_price': 40000, 'selling_price': 50000, 'discount': 15, 'stock': 10}

# --------------------------------------------------
# 4. DICTIONARY
# --------------------------------------------------

product = {
    "name": "Laptop",
    "cost_price": 40000,
    "selling_price": 50000,
    "discount": 10
}

print("\nProduct:", product)

# Access dictionary values
print("Product Name:", product["name"])
print("Cost Price:", product["cost_price"])

# Add new key
product["stock"] = 10

# Update value
product["discount"] = 15

print("Updated Product:", product)
#--------------------------------------------------
#output
#--------------------------------------------------
Product: {'name': 'Laptop', 'cost_price': 40000, 'selling_price': 50000, 'discount': 10}
Product Name: Laptop
Cost Price: 40000
Updated Product: {'name': 'Laptop', 'cost_price': 40000, 'selling_price': 50000, 'discount': 15, 'stock': 10}

# --------------------------------------------------
# 5. STRING METHODS
# --------------------------------------------------

product_name = "  laptop computer  "

print("\nOriginal Name:", product_name)

print("Upper:", product_name.upper())
print("Lower:", product_name.lower())
print("Title:", product_name.title())
print("Strip:", product_name.strip())
print("Replace:", product_name.replace("laptop", "gaming laptop"))

# Check string
print("Starts with laptop:", product_name.strip().startswith("laptop"))
print("Ends with computer:", product_name.strip().endswith("computer"))
#--------------------------------------------------
#output
#--------------------------------------------------
name = "  laptop computer  "
print("\nOriginal:", name)
print("Upper:", name.upper())
print("Lower:", name.lower())
print("Title:", name.title())
print("Strip:", name.strip())
print("Replace:", name.replace("laptop", "gaming laptop"))
print("Startswith:", name.strip().startswith("laptop"))
print("Endswith:", name.strip().endswith("computer"))

# --------------------------------------------------
# 6. BUSINESS DISCOUNT CALCULATION
# --------------------------------------------------

cost_price = 40000
selling_price = 50000
discount_percent = 10

discount_amount = selling_price * discount_percent / 100

final_price = selling_price - discount_amount

profit = final_price - cost_price

print("\n----- DISCOUNT & PROFIT -----")
print("Cost Price:", cost_price)
print("Selling Price:", selling_price)
print("Discount:", discount_percent, "%")
print("Discount Amount:", discount_amount)
print("Final Price:", final_price)
print("Profit:", profit)
#--------------------------------------------------
#output
#--------------------------------------------------
Cost Price: 40000
Selling Price: 50000
Discount: 10 %
Discount Amount: 5000.0
Final Price: 45000.0
Profit: 5000.0

# --------------------------------------------------
# 7. LIST COMPREHENSION
# --------------------------------------------------

prices = [10000, 20000, 30000, 40000, 50000]

# Add 10% discount to every product
discounted_prices = [price - (price * 10 / 100) for price in prices]

print("\nOriginal Prices:", prices)
print("10% Discount Prices:", discounted_prices)

# Find products above 30000
expensive_products = [price for price in prices if price > 30000]

print("Products above 30000:", expensive_products)
#--------------------------------------------------
#output
#--------------------------------------------------
Original Prices: [10000, 20000, 30000, 40000, 50000]
10% Discount Prices: [9000.0, 18000.0, 27000.0, 36000.0, 45000.0]
Products above 30000: [40000, 50000]

# --------------------------------------------------
# 8. DICTIONARY COMPREHENSION
# --------------------------------------------------

product_prices = {
    "Mobile": 20000,
    "Laptop": 50000,
    "Tablet": 30000,
    "Headphones": 5000
}

# Apply 10% discount to all products
discounted_products = {
    product: price - (price * 10 / 100)
    for product, price in product_prices.items()
}

print("\nOriginal Product Prices:")
print(product_prices)

print("Discounted Product Prices:")
print(discounted_products)
#---------------------------------------------------
#output
#----------------------------------------------------
Original Product Prices:
{'Mobile': 20000, 'Laptop': 50000, 'Tablet': 30000, 'Headphones': 5000}
Discounted Product Prices:
{'Mobile': 18000.0, 'Laptop': 45000.0, 'Tablet': 27000.0, 'Headphones': 4500.0}

# --------------------------------------------------
# 9. PROFIT USING DICTIONARY
# --------------------------------------------------

cost_prices = {
    "Mobile": 15000,
    "Laptop": 40000,
    "Tablet": 22000,
    "Headphones": 3000
}

selling_prices = {
    "Mobile": 20000,
    "Laptop": 50000,
    "Tablet": 30000,
    "Headphones": 5000
}

# Calculate profit for each product
profits = {
    product: selling_prices[product] - cost_prices[product]
    for product in selling_prices
}

print("\n----- PRODUCT PROFITS -----")
print(profits)
#--------------------------------------------------
#output
#-------------------------------------------------
{'Mobile': 5000, 'Laptop': 10000, 'Tablet': 8000, 'Headphones': 2000}

# --------------------------------------------------
# 10. PROFIT STATUS USING COMPREHENSION
# --------------------------------------------------

profit_status = {
    product: "Profit" if amount > 0 else "Loss"
    for product, amount in profits.items()
}

print("\nProfit Status:")
print(profit_status)
#--------------------------------------------------
#output
#--------------------------------------------------
{'Mobile': 'Profit', 'Laptop': 'Profit', 'Tablet': 'Profit', 'Headphones': 'Profit'}


# --------------------------------------------------
# FINAL BUSINESS SUMMARY
# --------------------------------------------------

total_profit = sum(profits.values())

print("\n==============================")
print("       BUSINESS SUMMARY")
print("==============================")
print("Total Products:", len(product_prices))
print("Total Profit:", total_profit)

if total_profit > 0:
    print("Business Status: PROFIT")
else:
    print("Business Status: LOSS")
#-------------------------------------------------------
output
#--------------------------------------------------------
Total Products: 4
Total Profit: 25000
Business Status: PROFIT

  
