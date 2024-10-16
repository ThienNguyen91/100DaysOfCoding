from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizInteface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg= THEME_COLOR, padx= 20, pady= 20)
        self.score_label = Label(text= "score: 0", fg= "white", bg= THEME_COLOR)
        self.score_label.grid(row= 0, column= 1)
        self.canvas = Canvas(width= 300, height= 250, bg= "white")
        self.question_text = self.canvas.create_text(150, 125,  text= "Some question text", fill= THEME_COLOR, font=("Ariel", 20, "italic"), width=280)
        self.canvas.grid(column= 0, row= 1, columnspan= 2, pady= 50)

        true_image = PhotoImage(file= "images/true.png")
        self.true_but = Button(image= true_image, highlightthickness= 0, command= self.answer_true)
        self.true_but.grid(column= 0, row= 2)
        false_image = PhotoImage(file= "images/false.png")
        self.false_but = Button(image= false_image, highlightthickness= 0, command= self.answer_false)
        self.false_but.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if not self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text= "You have reached the end")
            self.true_but.config(state= "disabled")
            self.false_but.config(state="disabled")
        else:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
    def answer_true(self):
        result = self.quiz.check_answer("true")
        self.give_feedback(result)
    def answer_false(self):
        result = self.quiz.check_answer("false")
        self.give_feedback(result)
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg= "green")
        if not is_right:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
