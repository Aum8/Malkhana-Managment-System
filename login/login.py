import tkinter as tk
from tkinter import messagebox
import login.logindb as logindb
import home.Homepage as Homepage  # Import the logindb module

root = None
entry_username = None
entry_password = None

def check_login():
    global entry_username, entry_password, root
    username = entry_username.get()
    password = entry_password.get()

    if logindb.check_credentials(username, password):
        messagebox.showinfo("Success", "Login successful!")
        root.destroy()  
        Homepage.open_homepage()  
    else:
        messagebox.showerror("Error", "Wrong username or password")

def initloginpage():
    global entry_username, entry_password, root
    root = tk.Tk()
    root.state('zoomed') 
    root.title("Login Page")

  
    logindb.initialize_db()

    label_username = tk.Label(root, text="User ID:")
    label_password = tk.Label(root, text="Password:")
    entry_username = tk.Entry(root)
    entry_password = tk.Entry(root, show="*") 
    button_login = tk.Button(root, text="Login", command=check_login)

    label_username.pack(pady=10)
    entry_username.pack(pady=5)
    label_password.pack(pady=10)
    entry_password.pack(pady=5)
    button_login.pack(pady=20)

    root.mainloop()
