# from msilib.schema import ListBox
# from re import M
import tkinter as tk
from tkinter import *
from tkinter import simpledialog,messagebox
# import pywhatkit
import db as DB
# Setup window
# from random_password import Generator_GUI
import random_password
import strong_check

window = tk.Tk()
global is_on
is_on = True

    

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
    global is_on
#Create Buttons
    password_strength = tk.Button(window, text="Strength Check",font=("Helvetica", 8),command=strong_check.PasswordStrengthChecker)
    password_strength.place(x=30,y=30)

    generate_password = tk.Button(window, text="Generate Password",font=("Helvetica", 8),command=random_password.Generator_GUI)
    generate_password.place(x=130,y=30)

    add_new_password_button = tk.Button(window, text="Add New Password",font=("Helvetica", 8), command=lambda:add_new_password())
    add_new_password_button.place(x=250,y=30)

    delete_password_button = tk.Button(window, text="Delete Password", font=("Helvetica", 10), command=lambda: delete_password())
    delete_password_button.place(x=440,y=80)

    open_website_button = tk.Button(window,text="Open Website",font=("Helvetica", 10),command=lambda: open_website())
    open_website_button.place(x=560,y=80)

    show_password_button = tk.Button(window,text="Show Password",font=("Helvetica", 10),command=lambda:show_password_toggle())
    show_password_button.place(x=670,y=80)
#Create Titles
    title_website = tk.Label(window,text="Website",font=("Helvetica", 9))
    title_website.place(x=80,y=120)

    title_email = tk.Label(window,text="Email/Username",font=("Helvetica", 9))
    title_email.place(x=200,y=120)

    title_password = tk.Label(window,text="Password",font=("Helvetica", 9))
    title_password.place(x=380,y=120)
def add_new_password():
    # website = popup("website")
    website = popup("Website")
    email = popup("email/username")
    password = popup("password")
    DB.insert_details(website,email,password)
    task_list()

def task_list():
    global list1
    global is_on
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
    for website, email, password, hash_password in records:
        id1 += 1
        print("is on : " + str(is_on))
        if is_on:
            show = str(id1) + "   " + website + "   " + email + "  " + hash_password + "\n"
            print("hash : " + hash_password)
        else:
            show = str(id1) + "   " + website + "   " + email + "  " + password + "\n"
            print("not hash : " + password)


        print("Webstie " + str(len(website))) #15
        print("email/username " + str(len(email))) #22
        print("password " + str(len(password)))#15
        list1.insert(END, show)
def popup(name):
    answer = simpledialog.askstring("Enter info", name)
    return answer

def delete_password():
    try:
        val = int(list1.curselection()[0])
        data_list = (list1.get(val)).split("   ")
        print("Id number : " + data_list[0])
        # print("app.py : " + data_list[1])
        # print(len(data_list[1]))
        DB.delete_details(str(data_list[1]))
        DB.print_dataBase()
        task_list()
    except:
        # messagebox.showerror('Select Task', 'Please select task from task List')
        pass
def open_website():
    val = int(list1.curselection()[0])
    data_list = (list1.get(val)).split("   ")
    # print("app.py : " + data_list[1])
    # print(len(data_list[1]))
    website = data_list[1]
    print(website)
    pywhatkit.search(website)
def show_password_toggle():
    global is_on
    if is_on:
        is_on = False
        task_list()
    else:
        is_on = True
        task_list()




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