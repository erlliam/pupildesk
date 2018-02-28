from tkinter import *

root = Tk()
root.title("Pupildesk")
root.resizable(width=False, height=False)
root.geometry("{}x{}".format(640, 480))

user = []

username_label = Label(root, text="Username").grid(row=0, column=0)
password_label = Label(root, text="Password").grid(row=1, column=0)

username_entry = Entry(root)
username_entry.grid(row=0, column=1)
password_entry = Entry(root, show="*")
password_entry.grid(row=1, column=1)

def focus_next_widget(event):
    event.widget.tk_focusNext().focus()

def submit_data(event):
    user.append(username_entry.get())
    user.append(password_entry.get())
    print(user)

login = Button(root, text="Login", command=submit_data).grid(columnspan=2, row=2)
username_entry.bind("<Return>", focus_next_widget)
password_entry.bind("<Return>", submit_data)

root.mainloop()

