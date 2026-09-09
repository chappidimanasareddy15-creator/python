# ==========================================
# MOBILE SHOP - FUNCTIONS IN PYTHON
# ==========================================

# 1. DEFINING A FUNCTION
# A simple function without arguments

def shop_name():
    print("Welcome to Mobile World")


shop_name()
#-------------------------------------------
#output
#--------------------------------------------
Welcome to Mobile World

# ------------------------------------------
# 2. ARGUMENTS & PARAMETERS
# ------------------------------------------

# name and price are PARAMETERS
def mobile_details(name, price):
    print("Mobile Name:", name)
    print("Price:", price)


# Samsung and 25000 are ARGUMENTS
mobile_details("Samsung", 25000)
#---------------------------------------------
#output
#----------------------------------------------
Mobile Name: Samsung
Price: 25000

# ------------------------------------------
# 3. MULTIPLE ARGUMENTS
# ------------------------------------------

def mobile_info(brand, model, price):
    print("Brand:", brand)
    print("Model:", model)
    print("Price:", price)


mobile_info("Apple", "iPhone 15", 60000)
#---------------------------------------------
#output
#----------------------------------------------
Brand: Apple
Model: iPhone 15
Price: 60000

# ------------------------------------------
# 4. DEFAULT ARGUMENT
# ------------------------------------------

def mobile_discount(price, discount=10):
    discount_amount = price * discount / 100
    final_price = price - discount_amount
    return final_price


print("Discounted Price:",
      mobile_discount(30000))
#---------------------------------------------
#output
#---------------------------------------------
Discounted Price: 27000.0
Profit: 5000
Discount Amount: 4000.0
Final Price: 36000.0

# ------------------------------------------
# 5. RETURN VALUE
# ------------------------------------------

def calculate_profit(cost_price, selling_price):
    profit = selling_price - cost_price
    return profit


profit = calculate_profit(20000, 25000)

print("Profit:", profit)
#----------------------------------------------
#output
#----------------------------------------------
Profit: 5000
# ------------------------------------------
# 6. RETURN MULTIPLE VALUES
# ------------------------------------------

def mobile_sale(price, discount):
    discount_amount = price * discount / 100
    final_price = price - discount_amount

    return discount_amount, final_price


discount_amount, final_price = mobile_sale(40000, 10)

print("Discount Amount:", discount_amount)
print("Final Price:", final_price)
#-----------------------------------------------
#output
#-----------------------------------------------
Discount Amount: 4000.0
Final Price: 36000.0


# ------------------------------------------
# 7. LAMBDA FUNCTION
# ------------------------------------------

# Lambda function to calculate discount

discount = lambda price: price * 10 / 100

print("Lambda Discount:", discount(50000))


# Lambda function to calculate profit

profit = lambda cost, selling: selling - cost

print("Lambda Profit:", profit(30000, 35000))
#-----------------------------------------------
#output
#------------------------------------------------
Lambda Discount: 5000.0
Lambda Profit: 5000

# ------------------------------------------
# 8. LOCAL VARIABLE
# ------------------------------------------

def mobile_price():
    price = 25000       # Local variable
    print("Local Price:", price)


mobile_price()
#-------------------------------------------
#output
#------------------------------------------
Local Price: 25000

# ------------------------------------------
# 9. GLOBAL VARIABLE
# ------------------------------------------

shop_location = "Tirupati"     # Global variable


def show_shop():
    print("Shop Location:", shop_location)


show_shop()
#----------------------------------------------
#output
#----------------------------------------------
Shop Location: Tirupati
Shop: Mobile World

# ------------------------------------------
# 10. LOCAL + GLOBAL VARIABLE
# ------------------------------------------

shop_name_global = "Mobile World"


def shop_details():
    mobile_count = 50       # Local variable

    print("Shop:", shop_name_global)
    print("Mobile Stock:", mobile_count)


shop_details()
#----------------------------------------------
#output
#----------------------------------------------
Shop: Mobile World

# ------------------------------------------
# 11. RECURSION
# ------------------------------------------

# Function calling itself

def mobile_stock(count):

    if count == 0:
        return

    print("Mobile Stock:", count)

    mobile_stock(count - 1)


mobile_stock(5)
#----------------------------------------------
#output
#----------------------------------------------
Mobile Stock: 50
Mobile Stock: 5
Mobile Stock: 4
Mobile Stock: 3
Mobile Stock: 2
Mobile Stock: 1

# ------------------------------------------
# 12. RECURSION - FACTORIAL
# ------------------------------------------

def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)


print("Factorial:", factorial(5))
#----------------------------------------------
#output
#-----------------------------------------------
Factorial: 120

# ==========================================
# FINAL MOBILE SHOP CALCULATION
# ==========================================

def mobile_bill(price, quantity, discount):

    total = price * quantity

    discount_amount = total * discount / 100

    final_bill = total - discount_amount

    return total, discount_amount, final_bill


total, discount_amount, final_bill = mobile_bill(
    25000, 2, 10
)

print("\n===== MOBILE BILL =====")
print("Total Price:", total)
print("Discount:", discount_amount)
print("Final Bill:", final_bill)
#--------------------------------------------------
#output
#---------------------------------------------------
Total Price: 50000
Discount: 5000.0
Final Bill: 45000.0
