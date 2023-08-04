import tkinter as tk
import MalkhanaTable.additems.additems as a
import MalkhanaTable.checkout.checkoutpage as co
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
    
    
    add_button = tk.Button(malkhanapage_frame, text="વસ્તુઓ ઉમેરો",background="#FFFFFF", command=additemsclicked, font=("Helvetica", 12))
    add_button.pack(pady=20)

    view_button = tk.Button(malkhanapage_frame, text="વસ્તુઓ જુઓ",background="#FFFFFF", command=viewitemsclicked, font=("Helvetica", 12))
    view_button.pack(pady=20)

    checkout_button = tk.Button(malkhanapage_frame, text="વસ્તુઓ ચેકઆઉટ કરો",background="#FFFFFF",command=checkoutclicked, font=("Helvetica", 12))
    checkout_button.pack(pady=20)

    checkin_button = tk.Button(malkhanapage_frame, text="વસ્તુઓ ચેકઇન કરો",background="#FFFFFF",command=checkinclicked, font=("Helvetica", 12))
    checkin_button.pack(pady=20)

    


    logout = tk.Button(malkhanapage_frame, text="લૉગઆઉટ", command=logoutclicked,background="#FFFFFF", font=("Helvetica", 12))
    logout.pack(side='right', anchor=tk.NE, padx=12, pady=20)

    back_button = tk.Button(malkhanapage_frame, text="પાછા જાઓ", command=go_back, background="#FFFFFF",font=("Helvetica", 12))
    back_button.pack(side='right', anchor=tk.NE, padx=10,pady=20)

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

def checkinclicked():
    malkhana_destroyer()
    ci.CIpage(malkhanapage_frame)

def checkoutclicked():
    malkhana_destroyer()
    co.COpage(malkhanapage_frame)

def viewitemsclicked():
    malkhana_destroyer()
    v.viewitems(malkhanapage_frame)

def malkhana_destroyer():
    if malkhanapage_frame is not None:
        malkhanapage_frame.destroy()

#s
