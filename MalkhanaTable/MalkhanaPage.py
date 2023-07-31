import tkinter as tk
import MalkhanaTable.additems.additems as a
import MalkhanaTable.checkin.checkinFromFSL as ci
import home.Homepage as Homepage
import MalkhanaTable.viewitems.viewitems as v
import login.login as login

def mkpage(prev_homepage_frame):
    prev_homepage_frame.pack_forget()
    global malkhanapage_frame
    malkhanapage_frame = tk.Frame(prev_homepage_frame.master)
    malkhanapage_frame.pack()
    
    
    add_button = tk.Button(malkhanapage_frame, text="વસ્તુઓ ઉમેરો", command=additemsclicked)
    add_button.pack()
    add_button.pack(pady=20)

    view_button = tk.Button(malkhanapage_frame, text="વસ્તુઓ જુઓ", command=viewitemsclicked)
    view_button.pack()
    view_button.pack(pady=20)

    checkout_button = tk.Button(malkhanapage_frame, text="વસ્તુઓ ચેકઇન કરો",command=checkinclicked)
    checkout_button.pack()
    checkout_button.pack(pady=20)

    logout = tk.Button(malkhanapage_frame, text="લૉગઆઉટ", command=logoutclicked)
    logout.pack(side='right', anchor=tk.NE, padx=12, pady=10)

    back_button = tk.Button(malkhanapage_frame, text="પાછા જાઓ", command=go_back)
    back_button.pack(side='right', anchor=tk.NE, padx=10, pady=10)

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

def checkinclicked():
    malkhana_destroyer()
    ci.CIpage(malkhanapage_frame)

def viewitemsclicked():
    malkhanapage_frame.pack_forget()
    v.viewitems(malkhanapage_frame)

def malkhana_destroyer():
    if malkhanapage_frame is not None:
        malkhanapage_frame.destroy()
