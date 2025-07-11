from tkinter import *

    # Button action
def converter():
    miles_to_km = round(1.609 * float(miles_input.get()), 2)
    kilometer_result.config(text=miles_to_km)

    # Window
window = Tk()
window.title("Mile to Km converter")
window.minsize(300,200)
window.config(padx=50, pady=50)

    # Label
is_equal_to_label = Label(text="is equal to", font=("Courier", 15, "normal"))
is_equal_to_label.grid(column=0, row=1)
miles_label = Label(text="Miles", font=("Courier", 15, "normal"))
miles_label.grid(column=2, row=0)
kilometer_result = Label(text="0", font=("Courier", 15, "normal"))
kilometer_result.grid(column=1, row=1)
kilometer_label = Label(text="Km", font=("Courier", 15, "normal"))
kilometer_label.grid(column=2, row=1)

    # Input
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

    # Button
calculate_button = Button(width=10, text="Convert", command=converter)
calculate_button.grid(column=1, row=2)

window.mainloop()