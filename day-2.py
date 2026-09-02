# ==========================================
# STUDENT ATTENDANCE - PYTHON OPERATORS
# ==========================================

student_name = "Manasa"
total_days = 20
present_days = 18
absent_days = 2

print("===== STUDENT ATTENDANCE =====")
print("Student Name:", student_name)
print("Total Days:", total_days)
print("Present Days:", present_days)
print("Absent Days:", absent_days)
#--------------------------------------------
#output
#---------------------------------------------
Student Name: Manasa
Total Days: 20
Present Days: 18
Absent Days: 2

# ==========================================
# 1. ARITHMETIC OPERATORS
# ==========================================

print("\n===== ARITHMETIC OPERATORS =====")

# Addition
total = present_days + absent_days
print("Addition:", total)

# Subtraction
remaining = total_days - present_days
print("Subtraction:", remaining)

# Multiplication
double_present = present_days * 2
print("Multiplication:", double_present)

# Division
average = present_days / total_days
print("Division:", average)

# Floor Division
days_per_week = total_days // 5
print("Floor Division:", days_per_week)

# Modulus
remaining_days = total_days % 7
print("Modulus:", remaining_days)

# Power
example = present_days ** 2
print("Power:", example)
#----------------------------------------------
#output
#----------------------------------------------
Addition: 20
Subtraction: 2
Multiplication: 36
Division: 0.9
Floor Division: 4
Modulus: 6
Power: 324

# ==========================================
# 2. COMPARISON OPERATORS
# ==========================================

print("\n===== COMPARISON OPERATORS =====")

print("Present days == Total days:", present_days == total_days)
print("Present days != Total days:", present_days != total_days)
print("Present days > Absent days:", present_days > absent_days)
print("Present days < Total days:", present_days < total_days)
print("Present days >= 18:", present_days >= 18)
print("Absent days <= 2:", absent_days <= 2)
#---------------------------------------------------
#output
#---------------------------------------------------
Present days == Total days: False
Present days != Total days: True
Present days > Absent days: True
Present days < Total days: True
Present days >= 18: True
Absent days <= 2: True

# ==========================================
# 3. ASSIGNMENT OPERATORS
# ==========================================

print("\n===== ASSIGNMENT OPERATORS =====")

days = present_days
print("Original days:", days)

days += 1
print("After += 1:", days)

days -= 1
print("After -= 1:", days)

days *= 2
print("After *= 2:", days)

days //= 2
print("After //= 2:", days)
#-----------------------------------------------
#output
#-----------------------------------------------
Original days: 18
After += 1: 19
After -= 1: 18
After *= 2: 36
After //= 2: 18
# ==========================================
# 4. LOGICAL OPERATORS
# ==========================================

print("\n===== LOGICAL OPERATORS =====")

attendance = (present_days / total_days) * 100

print("Attendance:", attendance)

print("AND:", attendance >= 75 and present_days >= 10)
print("OR:", attendance >= 75 or absent_days <= 2)
print("NOT:", not attendance < 75)
#----------------------------------------------
#output
#-----------------------------------------------
Attendance: 90.0
AND: True
OR: True
NOT: True

# ==========================================
# 5. MEMBERSHIP OPERATORS
# ==========================================

print("\n===== MEMBERSHIP OPERATORS =====")

students = ["Manasa", "Rupa", "Dilli"]

print("Manasa in students:", "Manasa" in students)
print("Rahul in students:", "Rahul" in students)
print("Rahul not in students:", "Rahul" not in students)
#------------------------------------------------
#output
#------------------------------------------------
Manasa in students: True
Rahul in students: False
Rahul not in students: True

# ==========================================
# 6. IDENTITY OPERATORS
# ==========================================

print("\n===== IDENTITY OPERATORS =====")

present_status = True
attendance_status = present_status

print("Same object:", present_status is attendance_status)
print("Different object:", present_status is not False)
#--------------------------------------------
#output
#--------------------------------------------
Same object: True
Different object: True

# ==========================================
# FINAL ATTENDANCE
# ==========================================

print("\n===== FINAL RESULT =====")

print("Student:", student_name)
print("Attendance:", attendance, "%")

if attendance >= 75:
    print("Status: Eligible")
else:
    print("Status: Not Eligible")
    #-------------------------------------------
    #output
    #--------------------------------------------
    Student: Manasa
Attendance: 90.0 %
Status: Eligible
