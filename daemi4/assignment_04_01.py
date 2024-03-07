# Author: <Andri Benedikt>
# Date: <06-03-2024>
# Project: <assignment_04_01>
# Acknowledgements: <GPT til að "{highest_mean_value:.2f}">


students = {
    input("Student name: "): [float(input("Input grade number 1: ")), float(input("Input grade number 2: ")), float(input("Input grade number 3: "))],
    input("Student name: "): [float(input("Input grade number 1: ")), float(input("Input grade number 2: ")), float(input("Input grade number 3: "))],
    input("Student name: "): [float(input("Input grade number 1: ")), float(input("Input grade number 2: ")), float(input("Input grade number 3: "))],
    input("Student name: "): [float(input("Input grade number 1: ")), float(input("Input grade number 2: ")), float(input("Input grade number 3: "))]
    }
sorted_students = sorted(students)
highest_mean = ""
highest_mean_value = 0
print("Student list:")
for student in sorted_students:
    print(f'{student}: {students[student]}')
    if sum(students[student])/len(students[student]) > highest_mean_value:
        highest_mean = student
        highest_mean_value = sum(students[student])/len(students[student])
print("Student with highest average grade:")
print(f'{highest_mean} has an average grade of {highest_mean_value:.2f}')
