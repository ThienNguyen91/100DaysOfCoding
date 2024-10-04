from data import  question_data
from question_model import AddQuestion
from quiz_brain import QuizBrain


question_bank = [AddQuestion(q["question"], q["correct_answer"]) for q in question_data]
Start = QuizBrain(question_bank)
while Start.next_question():
    pass
