# Student Attendance Management
# Control Flow: if, elif, else, nested if,
# for loop, while loop, break, continue, pass


# Student details
student_name = "Manasa"
total_classes = 10
attended_classes = 8

# Calculate attendance percentage
attendance_percentage = (attended_classes / total_classes) * 100

print("===== STUDENT ATTENDANCE =====")
print("Student Name:", student_name)
print("Total Classes:", total_classes)
print("Attended Classes:", attended_classes)
print("Attendance Percentage:", attendance_percentage, "%")
#==================================================
#output
#==================================================
Student Name: Manasa
Total Classes: 10
Attended Classes: 8
Attendance Percentage: 80.0 %

# ------------------------------------------------
# 1. if, elif, else
# ------------------------------------------------

print("\n===== ATTENDANCE STATUS =====")

if attendance_percentage >= 75:
    print("Attendance Status: Eligible")

elif attendance_percentage >= 50:
    print("Attendance Status: Shortage")

else:
    print("Attendance Status: Not Eligible")
#=================================================
#output
#=================================================
Attendance Status: Eligible

# ------------------------------------------------
# 2. Nested if
# ------------------------------------------------

print("\n===== NESTED CONDITION =====")

if attendance_percentage >= 75:

    if attendance_percentage >= 90:
        print("Excellent Attendance")

    elif attendance_percentage >= 80:
        print("Very Good Attendance")

    else:
        print("Good Attendance")

else:
    print("Attendance is below 75%")
#================================================
#output
#================================================
Very Good Attendance

# ------------------------------------------------
# 3. FOR LOOP
# ------------------------------------------------

print("\n===== DAILY ATTENDANCE =====")

attendance = ["Present", "Present", "Absent", "Present", "Present"]

for day in attendance:
    print("Attendance:", day)
#================================================
#output
#================================================
Attendance: Present
Attendance: Present
Attendance: Absent
Attendance: Present
Attendance: Present

# ------------------------------------------------
# 4. FOR LOOP with CONTINUE
# ------------------------------------------------

print("\n===== PRESENT DAYS =====")

for day in attendance:

    if day == "Absent":
        continue

    print("Student was Present")
#==================================================
#output
#==================================================
Student was Present
Student was Present
Student was Present
Student was Present

# ------------------------------------------------
# 5. FOR LOOP with BREAK
# ------------------------------------------------

print("\n===== CHECKING ATTENDANCE =====")

for day in attendance:

    if day == "Absent":
        print("Absent day found!")
        break

    print("Present")
#=================================================
#output
#=================================================
Present
Present
Absent day found!

# ------------------------------------------------
# 6. PASS
# ------------------------------------------------

print("\n===== PASS EXAMPLE =====")

for day in attendance:

    if day == "Absent":
        pass

    print("Checking:", day)
#================================================
#output
#================================================
Checking: Present
Checking: Present
Checking: Absent
Checking: Present
Checking: Present

# ------------------------------------------------
# 7. WHILE LOOP
# ------------------------------------------------

print("\n===== WHILE LOOP =====")

day_number = 1

while day_number <= 5:
    print("Checking attendance for Day", day_number)

    day_number += 1
#=================================================
#output
#=================================================
Checking attendance for Day 1
Checking attendance for Day 2
Checking attendance for Day 3
Checking attendance for Day 4
Checking attendance for Day 5

# ------------------------------------------------
# 8. WHILE LOOP with BREAK
# ------------------------------------------------

print("\n===== WHILE LOOP WITH BREAK =====")

day_number = 1

while day_number <= 10:

    if day_number == 6:
        print("Attendance checking stopped.")
        break

    print("Day", day_number, "Present")

    day_number += 1
#================================================
#output
#================================================
Day 1 Present
Day 2 Present
Day 3 Present
Day 4 Present
Day 5 Present
Attendance checking stopped.


# ------------------------------------------------
# 9. WHILE LOOP with CONTINUE
# ------------------------------------------------

print("\n===== WHILE LOOP WITH CONTINUE =====")

day_number = 0

while day_number < 5:

    day_number += 1

    if day_number == 3:
        continue

    print("Checking Day", day_number)
#====================================================
#output
#====================================================
Checking Day 1
Checking Day 2
Checking Day 4
Checking Day 5

print("\n===== PROGRAM COMPLETED =====")
