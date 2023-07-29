import tkinter as tk
import login.login as login
import MalkhanaTable.MalkhanaPage as mk

def open_homepage(passing_frame):
    passing_frame.destroy() 
    global homepage_frame 
    if not homepage_frame:
        homepage_frame = tk.Frame(passing_frame.master)
        homepage_frame.pack()

        table_button = tk.Button(homepage_frame, text="Malkhana Table", command=clicked)
        table_button.pack(pady=20)
        homepage_frame.master.title("Homepage")
        homepage_frame.mainloop()

def open_homepage_r(return_frame):
    return_frame.pack_forget() 
    global homepage_frame 
    homepage_frame = tk.Frame(return_frame.master)
    homepage_frame.pack()

    table_button = tk.Button(homepage_frame, text="Malkhana Table", command=clicked)
    table_button.pack(pady=20)
    homepage_frame.master.title("Homepage")



def clicked():
    homepage_frame.pack_forget()
    mk.mkpage(homepage_frame)

homepage_frame = None  # Initialize the homepage_frame to None
