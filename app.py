from msilib.schema import ListBox
from re import M
import tkinter as tk
from tkinter import *
from tkinter import simpledialog

from click import password_option
import db as DB
# Setup window
window = tk.Tk()


    

def one_time_screen():
    clear_frame()
    window.geometry("600x300")

    tk.Label(window,text="Enter Password",font=("Helvetica", 12)).place(x=235,y=30)

    password1 = StringVar()
    text_box1 = tk.Entry(window,textvariable=password1,width=30)
    text_box1.place(x=200,y=70)
    

    tk.Label(window,text="Confirm Password",font=("Helvetica", 12)).place(x=235,y=130)
    password2 = StringVar()
    text_box2 = tk.Entry(window,textvariable=password2,width=30)
    text_box2.place(x=200,y=170)

    
    submit = tk.Button(window, text="Login",font=("Helvetica", 14),command=lambda:check_passwords(password1,password2))
    submit.place(x=255, y=250)

def clear_frame():
    for widget in window.winfo_children():
        widget.destroy()

def check_passwords(password1,password2):
    print("clicked")
    # print(password1)
    # print(password2)
    password1 = password1.get()
    password2 = password2.get()
    if DB.check_matches_passwords(password1,password2) == True:
        print("clicked")
        DB.insert_password(password1)
        main_screen()

def open_screen():
    clear_frame()
    window.title("Login into your database")
    window.geometry("500x500")

    login = tk.Button(window, text="Login",font=("Helvetica", 14))
    login.place(x=100, y=80)

    signUp = tk.Button(window, text="signUp",font=("Helvetica", 14))
    signUp.place(x=300, y=80)

def login_screen():
    pass


def signUp_screen():
    pass

def main_screen():
    clear_frame()
    window.geometry("800x350")
    details = DB.get_configuration_dataBase()
#Create Buttons
    generate_password = tk.Button(window, text="Generate Password",font=("Helvetica", 10),command=lambda:generate_random_password())
    generate_password.place(x=30,y=30)

    add_new_password_button = tk.Button(window, text="Add New Password",font=("Helvetica", 10), command=lambda:add_new_password())
    add_new_password_button.place(x=170,y=30)
#Create Titles
    title_website = tk.Label(window,text="Website",font=("Helvetica", 9))
    title_website.place(x=80,y=120)

    title_email = tk.Label(window,text="Email/Username",font=("Helvetica", 9))
    title_email.place(x=200,y=120)

    title_password = tk.Label(window,text="Password",font=("Helvetica", 9))
    title_password.place(x=380,y=120)
def task_list():
    global list1
    records = DB.get_configuration_dataBase()
    show = ""

    scrollbar = Scrollbar(window, width=15)
    scrollbar.place(x=710, y=155, relheight=0.5)
    list1 = Listbox(window, bg="#fff", font=("None", 13), relief='flat',
                    width=75, selectmode=SINGLE,
                    yscrollcommand=scrollbar.set)
    list1.place(x=20, y=155)
    scrollbar.config(command=list1.yview)
    id1 = 0
    for website, email, password in records:
        id1 += 1
        show = str(id1) + "   " + website + "   " + email + "  " + password + "\n"
        list1.insert(END, show)

def generate_random_password():
    pass
def add_new_password():
    # website = popup("website")
    website = popup("Website")
    email = popup("email/username")
    password = popup("password")
    DB.insert_details(website,email,password)
    task_list()

def popup(name):
    answer = simpledialog.askstring("Enter info", name)
    return answer


# Run the program
# DB.if_password_exist()
# if DB.if_password_exist() == True:
#     # print("true")
#     main_screen()
# else:
#     one_time_screen()
#     # print("false")
main_screen()
task_list()
window.mainloop()