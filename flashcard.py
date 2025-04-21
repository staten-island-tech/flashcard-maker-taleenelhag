import json

try:
    with open("flashcards_data.json", "r") as file:
        flashcards_data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    flashcards_data = []

# Class to define a flashcard
class Flashcard:
    def __init__(self, phrase, answer):
        self.phrase = phrase
        self.answer = answer

    def create_dict(self):
        return {self.phrase: self.answer}


ask = input("Create Flashcard? Y/N ").strip().lower()
while ask == 'y':
    phrase = input("Enter Word/Phrase: ")
    answer = input("Enter Definition/Answer: ")

    new_card = Flashcard(phrase, answer)
    flashcards_data.append(new_card.create_dict())

    ask = input("Create another flashcard? Y/N ").strip().lower()


with open("flashcards_data.json", "w") as file:
    json.dump(flashcards_data, file)


class Student:
    def __init__(self, name, score=0, streak=0):
        self.name = name
        self.score = score
        self.streak = streak

    def points(self):
        self.score += 1
        return self.score

    def streaks(self):
        self.streak += 1
        return self.streak

    def reset_streak(self):
        self.streak = 0

    def show_score(self):
        return self.score


student_name = input("Enter your name to start student mode: ")
student = Student(student_name)

switch = input("Switch to Student Mode? Y/N ").strip().lower()
while switch == 'y':
    for card in flashcards_data:
        for phrase, answer in card.items():
            user_attempt = input(f"{phrase}? ")

            if user_attempt.strip().lower() == answer.lower():
                print(f"Correct! Current Score: {student.points()}, Streak: {student.streaks()}")
            else:
                print(f"Incorrect. Streak broken. Score: {student.show_score()}")
                student.reset_streak()

    switch = input("Attempt another round? Y/N ").strip().lower()


