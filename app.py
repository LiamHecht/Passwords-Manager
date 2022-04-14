import tkinter as tk
from tkinter import *

# Setup window
window = tk.Tk()



def clear_frame():
    for widget in window.winfo_children():
        widget.destroy()


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



open_screen()
window.mainloop()

