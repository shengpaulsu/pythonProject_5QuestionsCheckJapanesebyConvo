from questions import Question
questions_prompts = [
    "1. Anata no nomae wa nan desu ka?\n(a) Nomae wa nan desuka?\n(b) Ann-san wa inai desu.\n(c) John desu.\n\n",
    "2. O ikutsu desu ka?\n(a) 25 sai desu.\n(b) 107 en.\n(c) 25 kutsu desu.\n\n",
    "3. Jimoto wa doko desu ka?\n(a) Watashi wa Osaka no shusshin desu.\n(b) Hokkado ni ikimasu.\n(c) Tokyo ni imasu.\n\n",
    "4. Kyodai wa imasu ka?\n(a) Hai, imasu.\n(b) Mitsu desu.\n(c) Ani wa kirai.\n\n",
    "5. Suki na tabemono wa nan desuka?\n(a) Kuruma ga suki desu.\n(b) Sushi desu.\n(c) Ramen tabetai desu.\n\n",
]
questions = [
    Question(questions_prompts[0], "c"),
    Question(questions_prompts[1], "a"),
    Question(questions_prompts[2], "a"),
    Question(questions_prompts[3], "a"),
    Question(questions_prompts[4], "b"),

]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+= 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)