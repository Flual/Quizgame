

# Creates a new game when called
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    # Nested forloop to display the Question with its answers
    for key in questions:
        print("# ---------------------- #")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# ----------------------

# Function to check if your guess matches your answer
def check_answer(answer, guess):

    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


# ----------------------

def display_score(correct_guesses, guesses):
    print("# ---------------------- #")
    print("Results")
    print("# ---------------------- #")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# ----------------------


def play_again():

    response = input("Do you want to play again?: (yes/no):")
    response = response.lower()

    if response == "yes":
        return True
    else:
        return False

# ----------------------


# Dictionary for the Questions
questions = {
    "The hammer and sickle is one of the most recognisable symbols of which political ideology?: ": "A",
    "Which Country did not Colonize the Americas: ": "B",
    "The Python Programming language is attributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A",
    "Construction of which of these famous landmarks was completed first?: ": "D"
}


# 2D list for Answers
options = [["A. Communism", "B. Fascism", "C. Liberalism", "D. Conservatism"],
           ["A. Russia", "B. Poland", "C. Denmark", "D. Courland"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. Blue Man Group"],
           ["A. Yes of Course", "B. The boys online say no", "C. Neither round not flat", "D. It used to be"],
           ["A. Empire State Building", "B. Suez Canal", "C. Eiffel Tower", "D. Big Ben Clock Tower"]]

new_game()

while play_again():
    new_game()

print("Bye!")