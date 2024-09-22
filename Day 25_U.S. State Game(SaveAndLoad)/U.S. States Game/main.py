import csv

import pandas
from turtle import Screen, Turtle
#FILE_DIR
INPUT_DIR = "50_states.csv"
SAVE_FILE = "save_file.csv"
IMAGE = "blank_states_img.gif"

#Turtle attribute
screen = Screen()
screen.title("U.S. States Game")
turtle = Turtle()
screen.addshape(IMAGE)
turtle.shape(IMAGE)
#player attribute
player_answer = None
auto_save = []
count = 0
#Read data
with open(INPUT_DIR) as f:
    f = pandas.read_csv(f)
    DATA = pandas.DataFrame(f)
    state_list = DATA.state.to_list()

#pen function
def pen(row):
    Pen = Turtle()
    Pen.hideturtle()
    Pen.penup()
    Pen.goto(row.x.item(), row.y.item())
    Pen.write(row.state.item())
#Save
def save(data_save):
    FIELD_NAME = ["state", "x", "y"]
    ROW = []
    for each_row in data_save:
        state = each_row.state.item()
        x = each_row.x.item()
        y = each_row.y. item()
        ROW.append({"state": state, "x": x, "y": y})
    with open("save_file.csv", "w", newline="") as file_save:
        writer = csv.DictWriter(file_save, fieldnames= FIELD_NAME)
        writer.writeheader()
        writer.writerows(ROW)
#load
def load(row):
    Pen = Turtle()
    Pen.hideturtle()
    Pen.penup()

    Pen.goto(row.x, row.y)
    Pen.write(row.state)
    auto_save.append(DATA[DATA.state == row.state])
while count < 50:
    player_answer = screen.textinput(f"{count}/50 States Correct", "What is your guess?").title()
    if player_answer == "Save":
        save(auto_save)
        break
    if player_answer == "Load":
        save_data = pandas.read_csv(SAVE_FILE).drop_duplicates()
        save_data.apply(load, 1)
    if player_answer in state_list:
        correct_row = DATA[DATA.state == player_answer]
        auto_save.append(correct_row)
        pen(correct_row)
        count += 1

screen.mainloop()