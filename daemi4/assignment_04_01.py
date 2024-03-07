# Author: <Andri Benedikt>
# Date: <06-03-2024>
# Project: <assignment_04_01>
# Acknowledgements: <>


students = {
    input("Student name: "): [int(input("Input grade number 1: ")), int(input("Input grade number 2: ")), int(input("Input grade number 3: "))],
    input("Student name: "): [int(input("Input grade number 1: ")), int(input("Input grade number 2: ")), int(input("Input grade number 3: "))],
    input("Student name: "): [int(input("Input grade number 1: ")), int(input("Input grade number 2: ")), int(input("Input grade number 3: "))],
    input("Student name: "): [int(input("Input grade number 1: ")), int(input("Input grade number 2: ")), int(input("Input grade number 3: "))]
    }
sorted_students = sorted(students)
highest_mean = 0
for student in sorted_students:
    print(students[student])