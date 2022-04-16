from msilib.schema import ListBox
from re import M
import tkinter as tk
from tkinter import *
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
    window.geometry("700x350")
    canvas = Canvas(
    window,
    bg="#ffffff",
    height=350,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge")
    canvas.place(x=0, y=0)
    scrollbar = Scrollbar(canvas, width=15)
    scrollbar.place(x=645, y=155, relheight=0.5)
    list1 = Listbox(canvas, bg="#fff", font=("None", 13), relief='flat',
                    width=40, selectmode=SINGLE,
                    yscrollcommand=scrollbar.set)


DB.if_password_exist()
if DB.if_password_exist() == True:
    # print("true") 
    main_screen()
else:
    one_time_screen()
    # print("false")
window.mainloop()