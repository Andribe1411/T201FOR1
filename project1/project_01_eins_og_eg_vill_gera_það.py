from random import randint;correct_counter = 0;name = input("What is your name? ");number_of_questions = int(input(f"Hello {name} welcome to the multiplication practice! \nHow many questions do you want? "))
for x in range(number_of_questions):
    number1 = randint(1, 10);number2 = randint(1, 10);answer = int(input(f"Q{x+1}: {number1} x {number2} = "))
    if answer == number1 * number2: print("Correct!"); correct_counter += 1
    else: print(f"Sorry, {number1} x {number2} = {number1 * number2}")
print("Thanks for the session", name,"\n",f"Correct answers = {correct_counter} wrong answers = {number_of_questions-correct_counter}","\n","Score =", int(correct_counter / number_of_questions * 100))
if int(correct_counter / number_of_questions * 100) == 100: print("Perfect!")
elif int(correct_counter / number_of_questions * 100) < 100 and int(correct_counter / number_of_questions * 100) >= 85: print("Excellent work!")
elif int(correct_counter / number_of_questions * 100) < 85 and int(correct_counter / number_of_questions * 100) >= 70: print("Not too bad")
elif int(correct_counter / number_of_questions * 100) < 70 and int(correct_counter / number_of_questions * 100) >= 50: print("Passing grade")
elif int(correct_counter / number_of_questions * 100) < 50: print("You need to practice more!")