import tkinter as tk
import MalkhanaTable.checkin.checkinFromFSL as f
import MalkhanaTable.checkin.checkinFromCourt as c
import MalkhanaTable.checkin.checkinFromFSL as ci
import home.Homepage as Homepage
import MalkhanaTable.MalkhanaPage as m

def CIpage(prev_homepage_frame):
    prev_homepage_frame.pack_forget()
    global CI_frame
    CI_frame = tk.Frame(prev_homepage_frame.master)
    CI_frame.master.title("Check in")
    CI_frame.pack()
    
    
    checkinFSL = tk.Button(CI_frame, text="Check in from FSL",command=fsl)
    checkinFSL.pack()
    checkinFSL.pack(pady=20)


    checkinCourt = tk.Button(CI_frame, text="Check in from Court",command=court)
    checkinCourt.pack()
    checkinCourt.pack(pady=20)

    Home = tk.Button(CI_frame, text="Home", command= go_home)
    Home.pack(side='right', anchor=tk.NE, padx=12, pady=10)

    back_button = tk.Button(CI_frame, text="Back", command=go_back)
    back_button.pack(side='right', anchor=tk.NE, padx=10, pady=10)


    

    CI_frame.mainloop()

def go_back():
    CI_frame.pack_forget()
    m.mkpage(CI_frame)
    

def go_home():
    CI_frame.pack_forget()
    Homepage.open_homepage_r(CI_frame)

def fsl():
    CI_frame.pack_forget()
    f.checkin_page(CI_frame)

def court():
    CI_frame.pack_forget()
    c.checkin_page_2(CI_frame)
