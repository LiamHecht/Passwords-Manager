from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
import zxcvbn  # You will need to install the zxcvbn library

class PasswordStrengthChecker:
    def __init__(self):
        self.window = Tk()
        self.window.title("Password Strength Checker")
        self.window.geometry("500x250")
        self.window.resizable(False, False)

        self.password_strength = StringVar()
        self.password_strength.set("")

        # Label Frame for Password Input
        self.input_frame = LabelFrame(self.window, text="Password Input")
        self.input_frame.pack(pady=10)

        self.password_label = Label(
            self.input_frame,
            text="Enter Password: "
        )
        self.password_label.grid(column=0, row=0)

        self.password_entry = Entry(
            self.input_frame,
            width=50
        )
        self.password_entry.grid(column=1, row=0)

        # Check Password Button
        self.check_button = Button(
            self.window,
            text="Check",
            command=self.check_password_strength
        )
        self.check_button.pack(pady=10)

        # Progress Bar
        self.progress_frame = LabelFrame(self.window, text="Password Strength")
        self.progress_frame.pack(pady=10)

        self.progress_bar = Progressbar(
            self.progress_frame,
            length=400,  # Increase the length to make it larger
            mode='determinate'
        )
        self.progress_bar.grid(column=0, row=0, columnspan=2)

        self.strength_label = Label(
            self.progress_frame,
            text="Strength: "
        )
        self.strength_label.grid(column=0, row=1)

        self.strength_value = Label(
            self.progress_frame,
            textvariable=self.password_strength
        )
        self.strength_value.grid(column=1, row=1)

        self.window.mainloop()

    def check_password_strength(self):
        password = self.password_entry.get()

        # Check password length (at least 6 characters)
        if len(password) < 6:
            messagebox.showerror("Password Error", "Password must be at least 6 characters long.")
            return

        result = zxcvbn.zxcvbn(password)
        strength = result['score']

        if strength < 2:
            # Password is weak, doesn't meet complexity requirements
            messagebox.showerror("Password Error", "Password is weak. It must contain at least one uppercase character, one lowercase character, one digit, and one special character.")
        else:
            # Update progress bar and strength label
            self.progress_bar['value'] = (strength / 4) * 100
            self.password_strength.set(result['feedback']['suggestions'])