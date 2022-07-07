#GUI = Graphical user interface

from tkinter import * 

window = Tk()

window.title("My Application")

window.geometry("300x300")

def submit_value():
    name = name_box.get()
    print(name)

label_title = Label(window, text="Registration form", font="times 15 bold").grid(row=0, column=3)

name_user = Label(window, text="Student Name")
name_user.grid(row=1, column=2)
branch_user = Label(window, text="Branch")
branch_user.grid(row=2, column=2)
gender_user = Label(window, text="Gender")
gender_user.grid(row=3, column=2)
phone_user = Label(window, text="Contact")
phone_user.grid(row=4, column=2)

name_value=StringVar
branch_value= StringVar
gender_value=StringVar
phone_user_value = StringVar

name_box = Entry(window, textvariable= name_value)
name_box.grid(row=1, column=3)
branch_box = Entry(window, textvariable= branch_value)
branch_box.grid(row=2, column=3)
gender_box = Entry(window, textvariable= branch_value)
gender_box.grid(row=3, column=3)
phone_box = Entry(window, textvariable= phone_user_value)
phone_box.grid(row=4, column=3)


Button(text="Submit", command=submit_value).grid(row=7, column=3)

window.mainloop()