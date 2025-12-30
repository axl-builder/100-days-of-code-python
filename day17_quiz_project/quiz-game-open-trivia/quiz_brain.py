class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        status = True
        if self.question_number == len(self.question_list):
            status = False
        return status

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you git it right!")
            self.score += 1
        else:
            print("thats wrong")
        print(f"the correct answer was: {correct_answer} ")
        print(f"your current score is: {self.score}/{self.question_number} ")   
        print("\n")

    def next_question(self):
        self.question_number += 1
        current_question = self.question_list[self.question_number - 1] 
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        if self.still_has_questions:
            self.check_answer(user_answer, current_question.answer)

