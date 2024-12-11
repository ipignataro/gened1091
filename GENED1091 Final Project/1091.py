## GENED1091 Final Project
## Bella Pignataro, December 2024

import csv
import random

def load_questions_from_csv(filename):
    """Load questions from a CSV file."""
    questions = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                questions.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    return questions

def filter_questions_by_week(questions, week):
    """Filter questions based on the week specified."""
    philosopher_map = {
        2: ["Confucius"],
        3: ["Confucius", "Mozi"],
        4: ["Confucius", "Mozi", "Mencius"],
        5: ["Confucius", "Mozi", "Mencius", "Laozi"],
        6: ["Confucius", "Mozi", "Mencius", "Laozi", "Inward Training"],
        7: ["Confucius", "Mozi", "Mencius", "Laozi", "Inward Training", "Zhuangzi"],
        8: ["Confucius", "Mozi", "Mencius", "Laozi", "Inward Training", "Zhuangzi", "Xunzi"],
        9: ["Confucius", "Mozi", "Mencius", "Laozi", "Inward Training", "Zhuangzi", "Xunzi", "Lord Shang"],
        10: ["Confucius", "Mozi", "Mencius", "Laozi", "Inward Training", "Zhuangzi", "Xunzi", "Lord Shang", "Han Feizi"],
    }

    # Get philosophers for the specified week or all if week >= 10
    philosophers = philosopher_map.get(week, philosopher_map[10])

    # Filter questions based on philosophers
    return [q for q in questions if q['philosopher'] in philosophers]

def run_quiz(questions):
    """Run the quiz with the given questions."""
    if not questions:
        print("No questions available to run the quiz.")
        return

    # Randomly select 10 questions
    selected_questions = random.sample(questions, min(10, len(questions)))

    score = 0

    print("\nWelcome to the Ancient Chinese Philosophy Quiz!")
    print("Answer the following questions by typing A, B, C, or D.\n")

    for index, question in enumerate(selected_questions, start=1):
        print(f"Question {index}: {question['question']}")
        print(f"A) {question['choice_a']}")
        print(f"B) {question['choice_b']}")
        print(f"C) {question['choice_c']}")
        print(f"D) {question['choice_d']}")
        answer = input("Your answer: ").strip().upper()

        if answer == question['correct_answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['correct_answer']}.")
            print(f"Explanation: {question['explanation']}\n")

    print(f"Quiz Complete! Your final score is {score}/{len(selected_questions)}.")
    if score == len(selected_questions):
        print("Amazing! You've mastered ancient Chinese philosophy!")
    elif score > len(selected_questions) / 2:
        print("Good job, philosopher! You have a solid understanding.")
    else:
        print("Keep learning! Ancient wisdom awaits.")

def main():
    filename = "questions.csv"  # Replace with the path to your CSV file
    questions = load_questions_from_csv(filename)

    try:
        week = int(input("What week of class are you on? (Enter a number): ").strip())
    except ValueError:
        print("Invalid input. Defaulting to week 10 (all questions).")
        week = 10

    if week < 2:
        print("You aren't ready yet, philosopher! You have so much to learn.")
        return

    filtered_questions = filter_questions_by_week(questions, week)
    run_quiz(filtered_questions)

if __name__ == "__main__":
    main()
