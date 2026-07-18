questions = [
    {
        "question": "Who developed Python?",
        "options": [
            "A. Dennis Ritchie",
            "B. Guido van Rossum",
            "C. James Gosling",
            "D. Bjarne Stroustrup"
        ],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": [
            "A. //",
            "B. <!-- -->",
            "C. #",
            "D. /* */"
        ],
        "answer": "C"
    },
    {
        "question": "Which of these is a Python list?",
        "options": [
            "A. {1, 2, 3}",
            "B. [1, 2, 3]",
            "C. (1, 2, 3)",
            "D. <1, 2, 3>"
        ],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": [
            "A. function",
            "B. define",
            "C. def",
            "D. fun"
        ],
        "answer": "C"
    },
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": [
            "A. 6",
            "B. 8",
            "C. 9",
            "D. 5"
        ],
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False values?",
        "options": [
            "A. String",
            "B. Integer",
            "C. Boolean",
            "D. Float"
        ],
        "answer": "C"
    },
    {
        "question": "Which function is used to get the length of a list?",
        "options": [
            "A. size()",
            "B. count()",
            "C. len()",
            "D. length()"
        ],
        "answer": "C"
    },
    {
        "question": "Which loop is used to iterate over a sequence?",
        "options": [
            "A. for",
            "B. repeat",
            "C. loop",
            "D. iterate"
        ],
        "answer": "A"
    },
    {
        "question": "Which module is used for mathematical functions in Python?",
        "options": [
            "A. random",
            "B. math",
            "C. calculation",
            "D. numbers"
        ],
        "answer": "B"
    },
    {
        "question": "Which statement is used to handle errors in Python?",
        "options": [
            "A. error-except",
            "B. try-except",
            "C. catch-throw",
            "D. check-error"
        ],
        "answer": "B"
    }
]

score = 0

name = input("Enter your name: ")
print("Welcome", name, "to the quiz!")

for answers in questions:
    print("\n" + answers["question"])

    for option in  answers["options"]:
        print(option)
    
    user_input = input("Your answer: ").upper()
    
    if user_input == answers["answer"]:
        print("Correct")
        score += 1

    elif user_input == "EXIT":
       print("Quiz ended!")
       break

    else:
       print("Wrong")

print("Final Score:",score)