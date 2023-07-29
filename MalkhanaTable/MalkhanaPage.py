import tkinter as tk
import MalkhanaTable.additems.additems as a
import home.Homepage as Homepage

def mkpage(prev_homepage_frame):
    prev_homepage_frame.pack_forget()
    global malkhanapage_frame
    malkhanapage_frame = tk.Frame(prev_homepage_frame.master)
    malkhanapage_frame.pack()
    home_button = tk.Button(malkhanapage_frame, text="Home", command=go_home)
    home_button.pack(side=tk.RIGHT, anchor=tk.N, padx=10, pady=10)

    back_button = tk.Button(malkhanapage_frame, text="Back", command=go_back)
    back_button.pack(side=tk.RIGHT, anchor=tk.N, padx=10, pady=10)

    add_button = tk.Button(malkhanapage_frame, text="Add Items",command=additemsclicked)
    add_button.pack()
    add_button.pack(pady=20)


    view_button = tk.Button(malkhanapage_frame, text="View Items")
    view_button.pack()
    view_button.pack(pady=20)


    checkin_button = tk.Button(malkhanapage_frame, text="Check In Items")
    checkin_button.pack()
    checkin_button.pack(pady=20)


    checkout_button = tk.Button(malkhanapage_frame, text="Check Out Items")
    checkout_button.pack()
    checkout_button.pack(pady=20)

    malkhanapage_frame.mainloop()

def go_back():
    malkhanapage_frame.pack_forget()
    Homepage.open_homepage_r(malkhanapage_frame)
    

def go_home():
    malkhanapage_frame.pack_forget()
    Homepage.open_homepage_r(malkhanapage_frame)

def additemsclicked():
    malkhanapage_frame.pack_forget()
    a.additems(malkhanapage_frame)

