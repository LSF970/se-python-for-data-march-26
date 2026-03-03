# Basic quiz game

# Set up bank of quiz questions
quiz = [
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "Is Python a snake or a programming language?", "answer": "programming language"},
    {"question": "Is Python a snake or a programming language?", "answer": "programming language"}
]

# Set initial score variable
score = 0

# Core quiz logic loop
for q in quiz:
    user_answer = input(q["question"] + " ")
    if user_answer.lower() == q["answer"].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

# Print end score
print("Your score:", score, "/", len(quiz))