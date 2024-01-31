# Author: <Andri Benedikt>
# Date: <29-01-2024>
# Project: <Skilaverkefni 1>
# Acknowledgements: <Fékk vin minn í tölvunafræði til að fara yfir kóðan fyrir python venjur og skipulag>

import random
#kommenta þetta út til að fá ekki alltaf sömu dæmi:
random.seed(1234)

#skilgreini teljara
correct_counter = 0
incorrect_counter = 0

#fæ breytur frá notanda
name = input("What is your name? ")
print("Hello ",name,", welcome to the multiplication practice!",sep="")
number_of_questions = int(input("How many questions do you want? "))


for _x in range(number_of_questions):
    #Tek tvær handahófskenndar tölur og margfalda þær saman
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10) 
    correct_answer = number1 * number2      

    #Fæ notandan til að giska á svarið og forritið lætur vita ef það er rétt eða rangt
    answer = int(input(f"What is {number1} x {number2}: "))
    if answer == correct_answer:
        print("Correct!")
        correct_counter += 1
    else:
        print(f"Sorry, {number1} x {number2} = {correct_answer}")
        incorrect_counter += 1

#Reikna stig notanda og prenta viðeigandi texta miðað við niðurstöðu notanda
if number_of_questions > 0:
    score = int(correct_counter / number_of_questions * 100)
else:
    score = 0

print("Thanks for the session", name)
print(f"Correct answers = {correct_counter}, wrong answers = {incorrect_counter}")
print(f"Score = {score}")

if score == 100:
    print("Perfect!")
elif 85 <= score < 100:
    print("Excellent work!")
elif 70 <= score < 85:
    print("Not too bad")
elif 50 <= score < 70:
    print("Passing grade")
else:
    print("You need to practice more!")