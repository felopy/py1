#Milonare geme
import random

def display_question(question, answers):
    print(question)
    for i in range(len(answers)):
        print(str(i + 1) + ". " + answers[i])

def get_player_answer():
    while True:
        try:
            player_answer = int(input("Your answer (enter the corresponding number): "))
            if 1 <= player_answer <= 4:
                return player_answer
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

def check_answer(player_answer, correct_answer):
    return player_answer == correct_answer

def millionaire_game(questions, answers, correct_answers, num_questions):
    total_correct = 0
    selected_indices = random.sample(range(len(questions)), num_questions)

    for index in selected_indices:
        display_question(questions[index], answers[index])
        player_answer = get_player_answer()
        
        if check_answer(player_answer, correct_answers[index]):
            print("Correct!\n")
            total_correct += 1
        else:
            print("Wrong answer! Try again.\n")

    print("Total correct answers: " + str(total_correct) + " out of " + str(num_questions))

if __name__ == "__main__":
    print("Welcome to the millionaire game")

    questions = [
        "What is the capital of Armenia?",
        "What is the capital of France?",
        "What is the capital of China?",
        "What is the capital of USA?",
        "What is the capital of Brazil?",
        "What is the capital of Georgia?",
        "What is the capital of Germany?",
        "What is the capital of Austria?",
        "What is the capital of Italy?",
        "What is the capital of Spain?",
        "What is the capital of the United Kingdom?",
        "What is the capital of Italy?",
        "What is the capital of the UAE?",
        "What is the capital of Portugal?",
        "What is the capital of Argentina?",
    ]

    answers = [
        ["Pekin", "Yerevan", "Gyumri", "Buenos Aires"],
        ["Gyumri", "Erevan", "Paris", "London"],
        ["Tbilisi", "Paris", "krasnodar", "Pekin"],
        ["Munchen", "Washington", "Pekin", "London"],
        ["Oslo", "Washington", "Pekin", "Brazil"],
        ["Tokio", "Washington", "Tbilisi", "Brazil"],
        ["Yerevan", "Berlin", "Lisbon", "Roma"],
        ["Minsk", "Erevan", "Viena", "Roma"],
        ["Barcelona", "Roma", "Lisbon", "Brazil"],
        ["London", "Paris", "Barcelona", "Madrid"],
        ["Varshava", "London", "Madrid", "Lisbon"],
        ["Qishnev", "Washington", "Roma", "Tbilisi"],
        ["Kopenhagen", "Washington", "Gyumri", "Abu Dhabi"],
        ["Sofia", "Lisbon", "Gyumri", "Buenos Aires"],
        ["Buenos Aires", "Washington", "Gyumri", "Atenq"],
    ]

    correct_answers = [2, 3, 4, 2, 4, 3, 2, 3, 2, 4, 2, 3, 4, 2, 1]

    num_questions = 10

    millionaire_game(questions, answers, correct_answers, num_questions)

        
