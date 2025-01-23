score = 0

quiz_questions = [
    "what is the most popular ship in Supernatural?",
    "who are the three main characters of Supernatural in order by age?",
    "what is the acronym for Supernatural?"
]

quiz_answers = [
    "Destiel",
    "Castiel, Dean, Sam",
    "SPN"
]
print(f"question: {"what is the most popular ship in Supernatural?"}")
user_answer = input("your answer: ")
if user_answer == "Destiel" :
    print("correct!")
    score += 1
else:
    print("no it aint")

print(f"question: {"who are the three main characters of Supernatural in order by age?"}")
user_answer = input("your answer: ")
if user_answer == "Castiel, Dean, Sam" :
    print("correct!")
    score += 1
else:
    print("no it aint")

print(f"question: {"what is the acronym for Supernatural"}")
user_answer = input("your answer: ")
if user_answer == "SPN" :
    print("correct!")
    score += 1
else:
    print("no it aint")

print(f"your score is: {score}")