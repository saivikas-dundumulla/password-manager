from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list.extend([choice(symbols) for _ in range(randint(2, 4))])
    password_list.extend([choice(numbers) for _ in range(randint(2, 4))])

    shuffle(password_list)
    password = "".join(password_list)
    pwd_entry.delete(0, END)
    pwd_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pwd_entry.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Invalid Data", message="Please don't leave any fields empty")
        return
    answer = messagebox.askyesno(title=f"{website}", message=f"Details\nEmail: {email}\nPassword: {password}\nDo you proceed to save?")
    if answer:
        with open("data.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")
        web_entry.delete(0, END)
        pwd_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=40, pady=40)
window.title("Password Manager")
# window.minsize(width=400, height=400)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

pwd_label = Label(text="Password:")
pwd_label.grid(row=3, column=0)

#Entry
web_entry = Entry(width=52)
web_entry.grid(row=1, column=1, columnspan=2, sticky="W", pady=4)
web_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2, sticky="W", pady=2)
email_entry.insert(END, "saivikas@gmail.com")

pwd_entry = Entry(width=32)
pwd_entry.grid(row=3, column=1, sticky="W", pady=2)

#Buttons
pwd_gen_btn = Button(text="Generate Password", command=generate_password)
pwd_gen_btn.grid(row=3, column=2, sticky="W", pady=2)

add_btn = Button(text="Add", width=44, command=save)
add_btn.grid(row=4, column=1, columnspan=2, sticky="W", pady=2)


window.mainloop()