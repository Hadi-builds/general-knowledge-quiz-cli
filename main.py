def main():
    score = 0
    total_questions = 3

    print("=" * 50)
    print("       THE GENERAL KNOWLEDGE QUIZ")
    print("=" * 50)

    # Question 1
    q1 = (
        input("\nQuestion 1: What is the capital of France?\nYour Answer: ")
        .strip()
        .lower()
    )
    if q1 == "paris":
        print("Correct! +1 point added to the score vault.")
        score += 1
    else:
        print("Incorrect! The correct answer was Paris.")

    # Question 2
    q2 = (
        input("\nQuestion 2: Which planet is known as the Red Planet?\nYour Answer: ")
        .strip()
        .lower()
    )
    if q2 == "mars":
        print("Correct! +1 point added to the score vault.")
        score += 1
    else:
        print("Incorrect! The correct answer was Mars.")

    # Question 3
    q3 = (
        input("\nQuestion 3: What is the largest ocean on Earth?\nYour Answer: ")
        .strip()
        .lower()
    )
    if q3 == "pacific" or q3 == "pacific ocean":
        print("Correct! +1 point added to the score vault.")
        score += 1
    else:
        print("Incorrect! The correct answer was Pacific Ocean.")

    # Final Output Delivery
    print("\n" + "=" * 50)
    print("                    FINAL RESULTS")
    print("=" * 50)
    print(f"Final Score: {score:>2} / {total_questions}")

    if score == total_questions:
        print("Performance: Outstanding! Perfect score.")
    elif score >= 1:
        print("Performance: Good attempt! Keep practicing.")
    else:
        print("Performance: Needs improvement.")
    print("=" * 50)


if __name__ == "__main__":
    main()
