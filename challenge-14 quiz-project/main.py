from question_model import Questions
from data import question_list
from quiz_brain import QuizBrain

question_bank = []

for i in question_list:
    question_bank.append(Questions(i['text'],i['answer']))


quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()