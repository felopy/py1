import random
import time

countries = {
    "Dania": "Kopenhagen",
    "Belarus": "Minsk",
    "Ukraine": "Kiev",
    "Serbia": "Belgrad",
    "England": "London",
    "Armenia": "Yerevan",
    "Ruminia": "Bucharest",
    "Bulgharia": "Sofia",
    "Brazil": "Brasilia",
    "Spain": "Madrid",
    "Austria": "Vienna",
    "China": "Beijing",
    "India": "Delhi",
    "Algeria": "Algiers",
    "Germany": "Berlin",
    "Moldova": "Chisinau",
    "Italy": "Rome",
    "Russia": "Moscow",
    "Poland": "Warsaw",
    "Norway": "Oslo"
}

countries_list = list(countries.keys())

print("Welcome to the Capital City Guessing Game!")
print("Guess the capital city of the displayed country.")

chances = 3
timelimit = 10

while True:
    random_country = random.choice(countries_list)
    correct_capital = countries[random_country]
    
    print("\nCountry:", random_country)
    starttime = time.time()
    user = input("Your guess: ")
    etime = time.time()
    eltime = etime - starttime
    
    if user.lower() == correct_capital.lower():
        print("Correct! Great job!")
    elif eltime > timelimit:
        print("Sorry, you ran out of time. The correct answer is", correct_capital)
    else:
        chances -= 1
        if chances > 0:
            print("Sorry, that's incorrect. You have", chances, "chance" if chances == 1 else "chances", "left.")
        else:
            print("Sorry, you've used all your chances. The correct answer is", correct_capital)
            break

print("Thanks for playing!")

