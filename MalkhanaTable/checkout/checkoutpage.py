import tkinter as tk
import home.Homepage as Homepage
import MalkhanaTable.checkout.checkoutCourt as c
import MalkhanaTable.checkout.checkoutFSL as f
import MalkhanaTable.MalkhanaPage as m

CO_frame = None

def COpage(prev_homepage_frame):
    prev_homepage_frame.destroy()
    global CO_frame
    checkout_page_destroyer()
    CO_frame = tk.Frame(prev_homepage_frame.master)
    CO_frame.master.title("ચેક આઉટ​")
    CO_frame.pack()

    checkoutFSL = tk.Button(CO_frame, text="FSL વિભાગને ચેકઆઉટ", command=fsl, background="#FFFFFF", font=("Helvetica", 12))
    checkoutFSL.pack()
    checkoutFSL.pack(pady=20)

    checkoutCourt = tk.Button(CO_frame, text="કોર્ટને ચેકઆઉટ", command=court, background="#FFFFFF", font=("Helvetica", 12))
    checkoutCourt.pack()
    checkoutCourt.pack(pady=20)

    Home = tk.Button(CO_frame, text="હોમપેજ", command=go_home, background="#FFFFFF", font=("Helvetica", 12))
    Home.pack(side='right', anchor=tk.NE, padx=12, pady=10)

    back_button = tk.Button(CO_frame, text="પાછા જાઓ", command=go_back, background="#FFFFFF", font=("Helvetica", 12))
    back_button.pack(side='right', anchor=tk.NE, padx=10, pady=10)

    CO_frame.mainloop()

def go_back():
    checkout_page_destroyer()
    m.mkpage(CO_frame)

def go_home():
    checkout_page_destroyer()
    Homepage.open_homepage_r(CO_frame)

def fsl():
    checkout_page_destroyer()
    f.checkouttoFSL_page(CO_frame)

def court():
    checkout_page_destroyer()
    c.checkouttocourt_page(CO_frame)

def checkout_page_destroyer():
    if CO_frame is not None:
        CO_frame.destroy()
