from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
import json

FONTNAME = "Montserrat"
BEIGE = "beige"
BLACK = "black"
WHITE = "white"

# ---------------------------- WEBSITE SEARCH ------------------------------- #
# The user enters a website to check whether it has already been added to the list.
# If it has, they also check the email and password used on that website.
def search():
    with open("passwords.json", "r") as file:
        data = json.load(file)
        website = website_input.get()
        try:
            messagebox.showinfo(message=f"E-mail: {data[website]["email"]}\nPassword: {data[website]["password"]}")
        except KeyError:
            messagebox.showinfo(message="This website is not in this database")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Lists of possible characters for the password
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M',
           'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','#','$','%','&','(',')','*','+']

def generate_password():
    password_input.delete(0, END)
    # List comprehension
    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]
    password_list = password_letters + password_symbols + password_numbers
    # Password chars get shuffled randomly
    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    # Variables
    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()
    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }

    # Check if there are any empty fields
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Missing field(s)", message="Please, don't leave any fields empty")
    else:
        # Confirm if the user typed correctly
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nE-mail: {email}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            try:
                # Reading JSON file
                with open("passwords.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("passwords.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                # Updating JSON file
                data.update(new_data)
                # Writing into JSON file
                with open("passwords.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                # Clearing the entries
                website_input.delete(0, END)
                email_username_input.delete(0, END)
                email_username_input.insert(0, "@gmail.com")
                password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Generator")
window.config(bg=BEIGE, padx=20, pady=20, width=500, height=500)

# Logo
canvas = Canvas(width=200, height=200, bg=BEIGE, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100,image=logo)
canvas.grid(column=1, row=0)

# Labels
website_text = Label(text="Website:", fg=BLACK, bg=BEIGE, font=(FONTNAME, 12, "normal"))
website_text.grid(column=0, row=1)

email_username_text = Label(text="Email/Username:", fg=BLACK, bg=BEIGE, font=(FONTNAME, 12, "normal"))
email_username_text.grid(column=0, row=2)

password_text = Label(text="Password", fg=BLACK, bg=BEIGE, font=(FONTNAME, 12, "normal"))
password_text.grid(column=0, row=3)

# Inputs
website_input = Entry(width=21, bg=WHITE)
website_input.grid(column=1, row=1)
website_input.focus()

email_username_input = Entry(width=35, bg=WHITE)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(0, "@gmail.com")

password_input = Entry(width=21, bg=WHITE)
password_input.grid(column=1, row=3)

# Buttons
search_btn = Button(width=10, text="Search", command=search)
search_btn.grid(column=2, row=1)

generate_password_btn = Button(width=10, text="Generate Password", command=generate_password)
generate_password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=33, command=add)
add_btn.grid(columnspan=2, column=1, row=4)






window.mainloop()