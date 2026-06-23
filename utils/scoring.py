def calculate_score(
        questions,
        user_answers
):

    score = 0

    results = []

    for q, ans in zip(
            questions,
            user_answers
    ):

        correct = (
            ans == q["answer"]
        )

        if correct:
            score += 1

        results.append(
            {
                "question":
                q["question"],

                "selected":
                ans,

                "correct_answer":
                q["answer"],

                "is_correct":
                correct,

                "explanation":
                q["explanation"]
            }
        )

    return score, results