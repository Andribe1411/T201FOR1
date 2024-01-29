# Author: <Andri Benedikt>
# Date: <29-01-2024>
# Project: <Skilaverkefni 1>
# Acknowledgements: <Fékk vin minn í tölvunafræði til að fara yfir kóðan fyrir python venjur og skipulag>

import random
#Af kommenta þetta til að fá alltaf sömu tölur
#random.seed(1234)

#skilgreini teljara
counter = 1
correct_counter = 0
incorrect_counter = 0

#fæ breytur frá notanda
name = input("What is your name? ")
print("Hello",name,"welcome to the multiplication practice!")
number_of_questions = int(input("How many questions do you want? "))


while counter <= number_of_questions:
    #Tek tvær handahófskenndar tölur og margfalda þær saman
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10) 
    correct_answer = number1 * number2 

    #Fæ notandan til að giska á svarið og forritið lætur vita ef það er rétt eða rangt
    print(f"Q{counter}: {number1} x {number2}",end="")
    answer = int(input(" = "))
    if answer == correct_answer:
        print("Correct!")
        correct_counter += 1
    else:
        print(f"Sorry, {number1} x {number2} = {correct_answer}")
        incorrect_counter += 1
    counter += 1

#reikna stig notanda og prenta viðeigandi texta miðað við niðurstöðu notanda
score = int(correct_counter / number_of_questions * 100)
print("Thanks for the session", name)
print(f"Correct answers = {correct_counter} wrong answers = {incorrect_counter}")
print("Score =", score)
if score == 100:
    print("Perfect!")
elif score < 100 and score >= 85:
    print("Excellent work!")
elif score < 85 and score >= 70:
    print("Not too bad")
elif score < 70 and score >= 50:
    print("Passing grade")
elif score < 50:
    print("You need to practice more!")