from tkinter import *
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def miles_to_km():
    try:
        miles = int(miles_input.get())
        km = miles *1.609
        result_label.config(text=km)
        return km
    except ValueError:
        return
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

#entry
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)


result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


Calc_but = Button(text= "Calculate", command=miles_to_km)
Calc_but.grid(column=1, row=3)


window.mainloop()