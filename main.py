from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters=[random.choice(letters) for char in range(nr_letters)]
    password_symbols=[random.choice(symbols) for char in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters+ password_symbols+ password_numbers
    random.shuffle(password_list)

    password="".join(password_list)
    password_input.insert(0,password)

    


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_input.get()
    email=email_input.get()
    password=password_input.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered:\nWebsite: {website}\nEmail/Username: {email}\nPassword: {password}")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
photo_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=photo_image)
canvas.grid(row=0,column=1)

website_label=Label(text="Website:")
website_label.grid(row=1,column=0)

email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)

password_label=Label(text="Password:")
password_label.grid(row=3,column=0)

website_input=Entry(width=35)
website_input.grid(row=1,column=1,columnspan=2)
website_input.focus()

email_input=Entry(width=35)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0,"pirutivi@gmail.com")

password_input=Entry(width=21)
password_input.grid(row=3,column=1)

password_button=Button(text="Generate Password",command=generate_password)
password_button.grid(row=3,column=2)

add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()