# General Knowledge Quiz Decision Engine

An interactive command-line quiz application engineered in Python, structured around the **IPOS (Input-Process-Output-Storage)** architectural framework.

Developed under the **DecodeLabs Industrial Training Program (Project 4)**.

---

## Core Technical Highlights

- **IPOS Architecture**: Establishes clean separation of concerns across data capture (Input), evaluation logic (Process), runtime feedback (Output), and session state tracking (Storage).
- **Data Sanitization Pipeline**: Mitigates human input variance and accidental whitespace errors by passing raw terminal input through chained `.strip().lower()` filters.
- **State Vault Management**: Implements integer-based accumulator logic (`score = 0`) to enforce strict numeric integrity and maintain persistent runtime state.
- **Deterministic Branching**: Employs clean `if-else` control flow gates to eliminate ambiguous logic gaps and ensure deterministic automated evaluation.
- **Dynamic F-String Delivery**: Leverages Python f-strings with precision formatting tokens (e.g., `{score:>2}`) to produce aligned, professional CLI output.

---

## Architecture (IPOS Workflow)

```
[ Input ]    --> Prompt user via input() & capture raw string
      ↓
[ Process ]  --> Sanitize via .strip().lower() & evaluate against reference solution
      ↓
[ Storage ]  --> Update session accumulator (score vault increment)
      ↓
[ Output ]   --> Deliver contextual feedback and formatted final results
```

---

## Getting Started

### Prerequisites
- Python 3.8 or higher.

### Running the Application

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/general-knowledge-quiz-cli.git](https://github.com/YOUR-USERNAME/general-knowledge-quiz-cli.git)
   cd general-knowledge-quiz-cli
   ```

2. Run the script:
   ```bash
   python main.py
   ```

---

## Sample Execution

```text
==================================================
       THE GENERAL KNOWLEDGE QUIZ
==================================================

Question 1: What is the capital of France?
Your Answer:   PaRiS  
Correct! +1 point added to the score vault.

Question 2: Which planet is known as the Red Planet?
Your Answer: mars
Correct! +1 point added to the score vault.

Question 3: What is the largest ocean on Earth?
Your Answer: atlantic
Incorrect! The correct answer was Pacific Ocean.

==================================================
                    FINAL RESULTS
==================================================
Final Score:  2 / 3
Performance: Good attempt! Keep practicing.
==================================================
```
