from tkinter import *
from random import randint
import pandas
from pandas import *
DATA_DIR = "data/japan_word.csv"

with open(DATA_DIR, "r") as file:
    data = pandas.read_csv(file)
    data_dict = data.to_dict(orient= "records")
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashy")
window.config(padx= 50, pady= 50, bg=BACKGROUND_COLOR)

#
def change_word():
    random_num = randint(0, len(data_dict)-1)



canvas = Canvas(width=800,height=526)
green_bg = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263, image=green_bg)
japan_text = canvas.create_text(400, 150, text="Japan", font= ("ariel", 40, "italic"))
vocab_text = canvas.create_text(400, 263, text= "", font= ("ariel", 60, "bold"))
canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column =0, row =1, columnspan = 2)

#Button
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image= wrong_img, command=change_word)
wrong_button.config(bg= BACKGROUND_COLOR, highlightthickness=0)
wrong_button.grid(column= 0, row= 2)


right_img = PhotoImage(file="images/right.png")
right_button = Button(image= right_img, command=change_word)
right_button.config(bg= BACKGROUND_COLOR, highlightthickness=0)
right_button.grid(column= 1, row= 2)

















window.mainloop()
