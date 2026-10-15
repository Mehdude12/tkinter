from tkinter import *

root = Tk()
root.title("Login app")
root.geometry("400x400")
frame = Frame(master=root, height=200, width=360, bg="#57baec")

lbl1 = Label(frame, text="Full name", bg="#2a88e6", fg="white", width=12)
lbl2 = Label(frame, text="Email id", bg="#2a88e6", fg="white", width=12)
lbl3 = Label(frame, text="Enter password", bg="#2a88e6", fg="white", width=12)

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="*")


def Display():
    name = name_entry.get()
    greet = f"Hey {name}"
    message = "\nCongrtulations for you new promotion to FIRED"
    textbox.insert(END, greet)
    textbox.insert(END, message)


textbox = Text(bg="#29ddd7", fg="black")

btn = Button(text="Create account", command=Display, bg="red")


frame.place(x=20, y=0)
lbl1.place(y=20, x=20)
name_entry.place(x=150, y=20)
lbl2.place(y=80, x=20)
email_entry.place(y=80, x=150)
lbl3.place(y=140, x=20)
pass_entry.place(y=140, x=150)
btn.place(x=130, y=210)
textbox.place(y=250)

root.mainloop()
