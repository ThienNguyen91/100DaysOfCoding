from data import  question_data
from question_model import AddQuestion
from quiz_brain import QuizBrain

question_bank = []
for eachQuestion in  question_data:
    question_text = eachQuestion["text"]
    question_answer = eachQuestion["answer"]
    newQuestion = AddQuestion(question_text, question_answer)
    question_bank.append(newQuestion)
Start = QuizBrain(question_bank)
while Start.next_question():
    pass