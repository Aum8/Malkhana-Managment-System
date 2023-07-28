import tkinter as tk
from tkinter import messagebox
import login.logindb as logindb
import home.Homepage as Homepage

root = None
login_frame = None
entry_username = None
entry_password = None

def check_login():
    global entry_username, entry_password, login_frame
    username = entry_username.get()
    password = entry_password.get()

    if logindb.check_credentials(username, password):
        messagebox.showinfo("Success", "Login successful!")
        login_frame.pack_forget()  # Hide the login frame
        Homepage.open_homepage(login_frame)
    else:
        messagebox.showerror("Error", "Wrong username or password")

def initloginpage():
    global entry_username, entry_password, login_frame, root
    root = tk.Tk()
    root.state('zoomed')
    root.title("Login Page")

    logindb.initialize_db()

    login_frame = tk.Frame(root)

    label_username = tk.Label(login_frame, text="User ID:")
    label_password = tk.Label(login_frame, text="Password:")
    entry_username = tk.Entry(login_frame)
    entry_password = tk.Entry(login_frame, show="*")
    button_login = tk.Button(login_frame, text="Login", command=check_login)

    label_username.pack(pady=10)
    entry_username.pack(pady=5)
    label_password.pack(pady=10)
    entry_password.pack(pady=5)
    button_login.pack(pady=20)

    login_frame.pack()  # Pack the login frame initially

    root.mainloop()
