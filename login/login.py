import tkinter as tk
from tkinter import messagebox
import login.logindb as logindb
import home.Homepage as Homepage

entry_password = None
entry_username = None
login_frame = None
oraora = "user id"

def check_login():
    global login_frame 
    username = entry_username.get()
    password = entry_password.get()

    if logindb.check_credentials(username, password):
        messagebox.showinfo("Success", "Login successful!")
        Homepage.open_homepage(login_frame)
    else:
        messagebox.showerror("Error", "Wrong username or password")

def initloginpage(prev_main_frame):
    prev_main_frame.destroy()
    global entry_username, entry_password, login_frame

    login_destroyer()

    login_frame = tk.Frame(prev_main_frame.master)
    
    login_frame.pack()
    label_heading = tk.Label(login_frame, text="માલખાના મેનેજમેન્ટ સિસ્ટમ", font=("Helvetica", 16, "bold"))
    label_station = tk.Label(login_frame, text="ગોત્રી પોલીસ સ્ટેશન", font=("Helvetica", 14))
    label_heading.pack(anchor=tk.W, pady=20)
    label_station.pack(anchor=tk.W, pady=(5,50))

    login_frame.master.title("Login page")
    logindb.initialize_db()
    global oraora
    
    

    label_username = tk.Label(login_frame, text=oraora)
    label_password = tk.Label(login_frame, text="Password:")
    entry_username = tk.Entry(login_frame)
    entry_password = tk.Entry(login_frame, show="*")
    button_login = tk.Button(login_frame, text="Login", command=check_login)
    changelang = tk.Button(login_frame,text="Change",command= lang)
    changeback = tk.Button(login_frame,text="Change back",command= lang2)

    label_username.pack(pady=10)
    entry_username.pack(pady=5)
    label_password.pack(pady=10)
    entry_password.pack(pady=5)
    button_login.pack(pady=20)
    changelang.pack(pady=20)
    changeback.pack(pady=20)

def lang():
    global oraora
    oraora = "Userrrrrr"
    login_destroyer()
    initloginpage(login_frame)
    
def lang2():
    global oraora
    oraora = "User ID"
    login_destroyer()
    initloginpage(login_frame)

def login_destroyer():
    if login_frame is not None:
        login_frame.destroy()
