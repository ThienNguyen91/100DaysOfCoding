from tkinter import *
from random import choice
import pandas
DATA_DIR = "data/words_to_learn.csv"
try:
    data = pandas.read_csv(DATA_DIR)
except FileNotFoundError:
    data = pandas.read_csv("data/french_word.csv")
data_dict = data.to_dict(orient= "records")

current_card = {}
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashy")
window.config(padx= 50, pady= 50, bg=BACKGROUND_COLOR)

#
def change_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(data_dict)
    canvas.itemconfig(img, image=front_bg)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(vocab_text, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func= flip_card)
def flip_card():
    canvas.itemconfig(language_text, text= "English", fill= "white")
    canvas.itemconfig(vocab_text, text= current_card["English"], fill= "white")
    canvas.itemconfig(img, image=back_bg)

flip_timer = window.after(3000, func= flip_card)
def user_choose_right():
    data_dict.remove(current_card)
    new_save = pandas.DataFrame(data_dict)
    new_save.to_csv("data/words_to_learn.csv", index= False)
    print(len(data_dict))
    change_word()

canvas = Canvas(width=800,height=526)
front_bg = PhotoImage(file="images/card_front.png")
back_bg = PhotoImage(file="images/card_back.png")
img = canvas.create_image(400,263, image=front_bg)
language_text = canvas.create_text(400, 150, text="French", font= ("ariel", 40, "italic"))
vocab_text = canvas.create_text(400, 263, text= "", font= ("ariel", 60, "bold"))
canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column =0, row =1, columnspan = 2)

#Button
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image= wrong_img, command=change_word)
wrong_button.config(bg= BACKGROUND_COLOR, highlightthickness=0)
wrong_button.grid(column= 0, row= 2)


right_img = PhotoImage(file="images/right.png")
right_button = Button(image= right_img, command=user_choose_right)
right_button.config(bg= BACKGROUND_COLOR, highlightthickness=0)
right_button.grid(column= 1, row= 2)
change_word()













window.mainloop()
