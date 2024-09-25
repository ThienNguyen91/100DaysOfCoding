import math
from tkinter import *
from tkinter import PhotoImage

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
sets = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    label1.config(text="Timer", fg=GREEN, font=(FONT_NAME, 35))
    checkmarks.config(text="")
    canvas.itemconfig(timer_text, text=f"00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_countdown(time):
    count_min = math.floor(time/ 60)
    count_sec = time % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if time >0:
        global timer
        timer = window.after(1000, start_countdown, time-1)
    else:
        count()
        marks = ""
        for _ in range(math.floor(sets/2)):
            marks += "✓"
        checkmarks.config(text= marks)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #




def count():
    global sets
    sets += 1
    if sets % 8 == 0:
        start_countdown(LONG_BREAK_MIN)
        label1.config(text="Long Break", fg=RED, font=(FONT_NAME, 30))
    elif sets % 2 == 0:
        start_countdown(SHORT_BREAK_MIN)
        label1.config(text="Short Break", fg=GREEN, font=(FONT_NAME, 30))
    else:
        start_countdown(WORK_MIN)
        label1.config(text="Pomodoro", fg=PINK)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#Timer Label
label1 = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
label1.grid(column= 1, row= 0)

#Canvas
canvas = Canvas(width=200,height=224,bg= YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file= "tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill= "white", font=("Georgia", 35, "bold"))
canvas.grid(column= 1, row= 1)


start_but = Button(text= "Start",highlightthickness=0, command=count)
start_but.grid(column= 0, row= 2)

reset_but = Button(text= "Reset",highlightthickness=0, command=reset)
reset_but.grid(column= 2, row= 2)

checkmarks = Label(text="", fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row= 3)
















window.mainloop()