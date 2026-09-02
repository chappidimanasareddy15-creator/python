# ==========================================
# STUDENT ATTENDANCE PROGRAM
# Variables, Data Types & Type Conversion
# ==========================================

# ---------- VARIABLES ----------

student_name = "Manasa"
student_id = 101
total_days = 20
present_days = 18
attendance_percentage = 90.5
is_present = True

print("===== STUDENT ATTENDANCE =====")

print("Student Name:", student_name)
print("Student ID:", student_id)
print("Total Working Days:", total_days)
print("Present Days:", present_days)
print("Attendance Percentage:", attendance_percentage)
print("Present Today:", is_present)
#-----------------------------------------------
#output
#-----------------------------------------------
Student Name: Manasa
Student ID: 101
Total Working Days: 20
Present Days: 18
Attendance Percentage: 90.5
Present Today: True

# ---------- DATA TYPES ----------

print("\n===== DATA TYPES =====")

print("student_name:", type(student_name))
print("student_id:", type(student_id))
print("attendance_percentage:", type(attendance_percentage))
print("is_present:", type(is_present))
#-----------------------------------------------
#output
#-----------------------------------------------
student_name: <class 'str'>
student_id: <class 'int'>
attendance_percentage: <class 'float'>
is_present: <class 'bool'>

# ---------- TYPE CONVERSION ----------

print("\n===== TYPE CONVERSION =====")

# String to Integer
total_days_string = "20"
total_days_integer = int(total_days_string)

print("String:", total_days_string)
print("After int conversion:", total_days_integer)
print("Type:", type(total_days_integer))
#-------------------------------------------------
#output
#-------------------------------------------------
String: 20
After int conversion: 20
Type: <class 'int'>

# String to Float
percentage_string = "90.5"
percentage_float = float(percentage_string)

print("\nString:", percentage_string)
print("After float conversion:", percentage_float)
print("Type:", type(percentage_float))
#-------------------------------------------------
#output
#-------------------------------------------------
String: 90.5
After float conversion: 90.5
Type: <class 'float'>

# Integer to Float
present_days_float = float(present_days)

print("\nInteger:", present_days)
print("After float conversion:", present_days_float)
print("Type:", type(present_days_float))
#--------------------------------------------------
#output
#--------------------------------------------------
Integer: 18
After float conversion: 18.0
Type: <class 'float'>


# Integer to String
student_id_string = str(student_id)

print("\nInteger:", student_id)
print("After str conversion:", student_id_string)
print("Type:", type(student_id_string))
#-------------------------------------------------
#output
#-------------------------------------------------
Integer: 101
After str conversion: 101
Type: <class 'str'>


# Float to Integer
percentage_integer = int(attendance_percentage)

print("\nFloat:", attendance_percentage)
print("After int conversion:", percentage_integer)
print("Type:", type(percentage_integer))
#------------------------------------------------
#output
#------------------------------------------------
Float: 90.5
After int conversion: 90
Type: <class 'int'>

# ---------- CALCULATE ATTENDANCE ----------

attendance = (present_days / total_days) * 100

print("\n===== FINAL ATTENDANCE =====")
print("Student:", student_name)
print("Attendance:", attendance, "%")
#-------------------------------------------------
#output
#-------------------------------------------------
Student: Manasa
Attendance: 90.0 %
