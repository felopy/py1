import random
import os

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

def propose_question():
    print("Propose a new question:")
    question = input("Question: ")
    answer_choices = input("Answer choices (comma-separated): ").split(",")
    correct_answer = int(input("Correct answer (enter the corresponding number): "))

    
    with open("quest.txt", "a") as f:
        f.write("\n" + question + "\n")
        f.write(",".join(answer_choices) + "\n")
        f.write(str(correct_answer) + "\n")

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
    

    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    print("Script directory:", script_directory)

    
    file_path = os.path.join(script_directory, "quest.txt")
    
    print("File path:", file_path)

    questions = []
    answers = []
    correct_answers = []

    try:
    
        with open(file_path) as f:  
            lines = f.read().splitlines()

            for i in range(0, len(lines), 3):
                question = lines[i]
                answer_choices = lines[i + 1].split(",")
                correct_answer = int(lines[i + 2])  

                questions.append(question)
                answers.append(answer_choices)
                correct_answers.append(correct_answer)  
    except FileNotFoundError as e:
        print("Error:", e)

    num_questions = 10
    millionaire_game(questions, answers, correct_answers, num_questions)

    propose = input("Do you want to propose a question? (y/n): ")
    if propose.lower() == "y":
        propose_question()

