
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])
    password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])


    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)



window = Tk()
canvas = Canvas(window, width=200, height=200)
window.config(padx=20, pady=20)
photoimage = PhotoImage(file='logo.png')
canvas.create_image((100,100),image = photoimage)
canvas.grid(row=0, column=1)





#label
website_label = Label(window, text="Website:")
website_label.grid(row = 1,column = 0)
email_label = Label(window, text="Email/Username:")
email_label.grid(row = 2,column = 0)
password_label = Label(window, text="password:")
password_label.grid(row = 3,column = 0)

#Entries
website_entry = Entry(width = 21)
website_entry.grid(row = 1,column = 1)
website_entry.focus()
email_entry = Entry(width = 35)
email_entry.grid(row = 2,column = 1,columnspan = 2)
email_entry.insert(0,"ahaankhan.ahaan@gmail.com")
password_entry = Entry(width = 21)
password_entry.grid(row = 3,column = 1)

def save():
    """runs when add button is clicked
        ,save data to file
        ,removes the current data after saving """
    website = website_entry.get()
    password= password_entry.get()
    email = email_entry.get()
    data_dict = {website:{"email":email,"password":password}}
    if website == "" or  password == "":
        messagebox.showerror(title="Error", message="Please fill all fields")
    else:
        try:
            with open("data.json","r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(data_dict, file, indent=4)
        else:
            data.update(data_dict)
            with open("data.json","w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
def find_password():
    website = website_entry.get()
    try:
        with open("data.json","r") as file:
            data_to_read = json.load(file)


    except FileNotFoundError:
        messagebox.showerror(title="Error", message="File not found")
    else:
       if website in data_to_read:
           email = data_to_read[website]['email']
           password = data_to_read[website]['password']
           messagebox.showinfo(title=website, message=f"email: {email} \n password: {password}")
       else:
           messagebox.showerror(title="Error", message="No data found for this website")



#buttons
generate_password_button = Button(text = "Generate Password",command = password_generator)
generate_password_button.grid(row = 3,column = 2)

search_button = Button(text = "Search",command = find_password,width = 13)
search_button.grid(row = 1,column = 2)

add_button = Button(text = "Add",width = 36,command = save)
add_button.grid(row = 4,column = 1,columnspan = 2)



window.mainloop()