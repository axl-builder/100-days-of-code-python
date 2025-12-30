class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self) -> bool:
        """Checks if there are questions left in the bank."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Fetches the next question and validates user input."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        
        # OWASP A03:2021 – Injection & Input Validation
        # Ensuring user input is handled safely and restricted to expected values.
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").strip().lower()
        
        while user_answer not in ["true", "false", "t", "f"]:
            user_answer = input("Invalid input. Please enter 'True' or 'False': ").strip().lower()
            
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        # Normalize input for comparison (Robustness)
        if user_answer[0] == correct_answer.lower()[0]:
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect.")
        
        print(f"The correct answer was: {correct_answer}")
        print(f"Current Score: {self.score}/{self.question_number}\n")
