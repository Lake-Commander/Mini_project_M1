def quiz_game():
    questions = [
        {"question": "What is the capital of Nigeria?", "answer": "abuja"},
        {"question": "What is 5 + 7?", "answer": "12"},
        {"question": "What is the chemical symbol for water?", "answer": "h2o"},
        {"question": "Who wrote 'All things fall apart'?", "answer": "chinua Achebe"},
        {"question": "What planet is known as the Red Planet?", "answer": "mars"}
    ]

    score = 0
    for i, q in enumerate(questions, 1):
        user_answer = input(f"Q{i}: {q['question']} ").strip().lower()
        if user_answer == q["answer"].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}\n")

    print(f"Your final score: {score}/{len(questions)}")

quiz_game()
