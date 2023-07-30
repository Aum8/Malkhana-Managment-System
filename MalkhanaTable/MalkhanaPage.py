import tkinter as tk
import MalkhanaTable.additems.additems as a
import MalkhanaTable.checkin.checkinpage as ci
import home.Homepage as Homepage
import MalkhanaTable.viewitems.viewitems as v
import login.login as login

malkhanapage_frame = None

def mkpage(prev_homepage_frame):
    prev_homepage_frame.destroy()

    global malkhanapage_frame
    malkhana_destroyer()
    malkhanapage_frame = tk.Frame(prev_homepage_frame.master)
    malkhanapage_frame.master.title("Malkhana page")
    malkhanapage_frame.pack()
    
    
    add_button = tk.Button(malkhanapage_frame, text="Add Items",command=additemsclicked)
    add_button.pack()
    add_button.pack(pady=20)


    view_button = tk.Button(malkhanapage_frame, text="View Items",command=viewitemsclicked)
    view_button.pack()
    view_button.pack(pady=20)

    checkout_button = tk.Button(malkhanapage_frame, text="Check Out Items")
    checkout_button.pack()
    checkout_button.pack(pady=20)

    logout = tk.Button(malkhanapage_frame, text="Logout", command=logoutclicked)
    logout.pack(side='right', anchor=tk.NE, padx=12, pady=10)

    back_button = tk.Button(malkhanapage_frame, text="Back", command=go_back)
    back_button.pack(side='right', anchor=tk.NE, padx=10, pady=10)


    

    malkhanapage_frame.mainloop()

def go_back():
    malkhana_destroyer()
    Homepage.open_homepage_r(malkhanapage_frame)
    
def logoutclicked():
    malkhana_destroyer()
    login.initloginpage(malkhanapage_frame)

def go_home():
    malkhana_destroyer()
    Homepage.open_homepage_r(malkhanapage_frame)

def additemsclicked():
    malkhana_destroyer()
    a.additems(malkhanapage_frame)

def viewitemsclicked():
    malkhana_destroyer()
    v.viewitems(malkhanapage_frame)

def malkhana_destroyer():
    if malkhanapage_frame is not None:
        malkhanapage_frame.destroy()


