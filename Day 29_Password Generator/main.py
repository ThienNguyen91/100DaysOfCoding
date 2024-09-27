from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
import pyperclip
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    Password_label_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = []
    [password_list.append(random.choice(letters)) for _ in range(random.randint(8, 10))]
    [password_list.append(random.choice(numbers)) for _ in range(random.randint(2, 4))]
    [password_list.append(random.choice(symbols)) for _ in range(random.randint(2, 4))]



    random.shuffle(password_list)

    password = "".join(password_list)
    Password_label_input.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_input.get()
    email = emailOrUsername_input.get()
    password = Password_label_input.get()
    if website and email and password:
        ask_ok = messagebox.askokcancel(title="Amaazon", message=f"These are the details entered: \nEmail: {email}"
                                                        f"\nPassword: {password} \n Is it ok to save?")
        if ask_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                messagebox.showinfo(title= "Title", message="Message")
    else:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    website_input.delete(0, END)
    Password_label_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx= 20, pady= 20)


canvas = Canvas(width=200,height=200)
tomato_img = PhotoImage(file= "logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column= 1, row= 0)

#Label
website_label = Label(text="Website: ")
website_label.grid(column= 0, row=1)
Password_label = Label(text="Email/Username: ")
Password_label.grid(column= 0, row=2)
emailOrUsername_label = Label(text="Password: ")
emailOrUsername_label.grid(column= 0, row=3)

#Entry
website_input = Entry(width=35)
website_input.grid(column= 1, row=1, columnspan= 2)
website_input.focus()
emailOrUsername_input = Entry(width=35)
emailOrUsername_input.grid(column= 1, row=2, columnspan= 2)
Password_label_input = Entry(width=35)
Password_label_input.grid(column=1, row=3, columnspan= 2)

gen_password = Button(text="Generate Password", command=password_generator)
gen_password.grid(column=2, row= 3)

add_but = Button(text="Add", width=36, command= add)
add_but.grid(column= 1, row= 4, columnspan=2, )




window.mainloop()