from tkinter import *

window = Tk()
window.minsize(width=300, height=200)
window.title("Miles to Km converter")
window.config(pady=40, padx=40, background="black")


# The function to actually convert
def miles_to_km():
    result = round(float(miles_input.get()) * 1.609, 2)
    label_result.config(text=result)


# Let's add all the elements
miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal = Label(text="is equal to ")
label_equal.grid(column=0, row=1)

label_result = Label(text=0)
label_result.grid(column=1, row=1)

label_km = Label(text="km")
label_km.grid(column=2, row=1)

button_calculate = Button(text="Calculate", command=miles_to_km)
button_calculate.grid(column=1, row=2)

window.mainloop()
