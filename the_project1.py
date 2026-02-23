import random
import os

def load_questions():
    with open("questions.txt", "r") as f:
        questions = f.readlines()
    return questions

def get_highscore():
    if not os.path.exists("highscore.txt"):
        with open("highscore.txt", "w") as f:
            f.write("0")
        return 0
    with open("highscore.txt", "r") as f:
        return int(f.read())

def update_highscore(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))

def start_quiz():
    questions = load_questions()
    selected_questions = random.sample(questions, 5)

    score = 0

    for q in selected_questions:
        parts = q.strip().split("|")
        question = parts[0]
        options = parts[1:5]
        correct_answer = parts[5]

        print("\n" + question)
        for i in range(4):
            print(f"{i+1}. {options[i]}")

        answer = input("Enter your answer (1-4): ")

        if answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print("\nQuiz Finished!")
    print("Your Score:", score, "/5")

    highscore = get_highscore()
    print("High Score:", highscore)

    if score > highscore:
        print("New High Score!")
        update_highscore(score)

if __name__ == "__main__":
    start_quiz()