from data import question_data
from quiz_brain import QuizBrain
from question_model import Question

question_bank = []
score = 0

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question(quiz.score)

print(f"You've completed the quiz\nYour final score was: {quiz.score}/{quiz.question_number}")