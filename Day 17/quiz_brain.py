

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def check_answer(self, user_answer):
        correct_answer = self.question_list[self.question_number].answer
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number+1}")

    def next_question(self):
        number = self.question_number
        if number == len(self.question_list):
            print("You've completed the quiz")
            print(f"Your final score was: {self.score}/{number}")
            return False
        ask = input(f"Q.{number+1}: {self.question_list[number].text}. (True/False)?: ")
        self.check_answer(ask)
        self.question_number += 1
        return True


