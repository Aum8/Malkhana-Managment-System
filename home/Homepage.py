import tkinter as tk
import MalkhanaTable.MalkhanaPage as mk

def open_homepage(prev_login_frame):
    prev_login_frame.pack_forget() 
    global homepage_frame 
    homepage_frame = tk.Frame(prev_login_frame.master)
    homepage_frame.pack()

    table_button = tk.Button(homepage_frame, text="Malkhana Table", command=clicked)
    table_button.pack(pady=20)
    prev_login_frame.master.title("Homepage")

def open_homepage_r(return_frame):
    return_frame.pack_forget() 
    global homepage_frame 
    homepage_frame = tk.Frame(return_frame.master)
    homepage_frame.pack()

    table_button = tk.Button(homepage_frame, text="Malkhana Table", command=clicked)
    table_button.pack(pady=20)
    homepage_frame.master.title("Homepage")

def clicked():
    mk.mkpage(homepage_frame)


