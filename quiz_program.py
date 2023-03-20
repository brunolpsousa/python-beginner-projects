# Dictionary that stores questions and answers
# Have a variable that tracks the score of the player
# Loop through the Dictionary using the key values pairs
# Display each question to the user and allow them to answer
# Tell them if they are right or wrong
# Show the final result when quiz is completed

quiz = {
    "q1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "q2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "q3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "q4": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "q5": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "q6": {
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"
    },
    "q7": {
        "question": "What is the capital of Austria?",
        "answer": "Vienna"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer: ")
    if answer.lower() == value['answer'].lower():
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!")
        print("The answer is: " + value['answer'] + "\n")
print("Your score is: " + str(score))
print("Your percentage is: " + str(int(score/7*100)) + "%")
