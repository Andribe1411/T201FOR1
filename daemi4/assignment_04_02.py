# Author: <Andri Benedikt>
# Date: <10-03-2024>
# Project: <assignment_04_02>
# Acknowledgements: <>

value_list = []
on = True
while on:
    value = input("")
    if value == "quit":
        on = False
        break
    try:
        value = int(value)
        value_list.append(value)
    except ValueError:
        print("Not a valid integer")
        continue




nums = value_list
max_length = 0
palindrome_sum = 0
max_palindrome = []

for i in range(len(nums)):
    for j in range(len(nums), i, -1):
        if nums[i:j] == nums[i:j][::-1]:
            current_length = j - i
            if current_length > max_length:
                max_length = current_length
                max_palindrome = nums[i:j]
                palindrome_sum = sum(max_palindrome)
                break 

print(", ".join(map(str, nums)))
print(f"The longest palindrome is {', '.join(map(str, max_palindrome))} with {max_length} elements and a sum of {palindrome_sum}")
