from question_model import Question
from data2 import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(text=question_text, answer=question_answer)
    question_bank.append(new_question)

game = QuizBrain(question_bank)

while game.still_has_questions():
    game.next_question()

print(f"youve completed the quiz")
print(f"your final score was: {game.score}/{game.question_number}")

