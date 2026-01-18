# quiz game

questions = ("How is the member of bigbang who got involved on the burning sun scandal? ",
             "What is the concept of Enhypen? ",
             "How many seconds are there in an hour? ")

options = (("A. TOP", "B. Seungri", "C. GDragon", "D. Taeyang"),
           ("A. Wolf", "B. Warriors", "C. Vampire", "D. Bird"),
           ("A. 3600 secs","B. 3660 secs.", "C. 8000 secs", "D. 5000 secs"))

answers = ("B", "C", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter your Answer: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} was the correct answer.")
    question_num += 1


print("----RESULTS----")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
    print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Score: {score}%")
