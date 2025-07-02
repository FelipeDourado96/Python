class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.questions_list = question_bank
        self.score = 0
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
    def next_question(self, score):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text} (True/False):\t")
        self.check_answer(user_answer, current_question)
    def check_answer(self, user_answer, current_question):
        if user_answer.lower() == current_question.answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was: {current_question.answer}.")
        print(f"({self.score}/{self.question_number})\n")