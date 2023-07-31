import tkinter as tk
import home.Homepage as Homepage
import login.login as login

FSLpage_frame = None

def fsl_page(prev_homepage_frame):
    prev_homepage_frame.destroy()
    global FSLpage_frame
    fsl_destroyer()
    FSLpage_frame = tk.Frame(prev_homepage_frame.master)
    FSLpage_frame.pack()

    logout = tk.Button(FSLpage_frame, text="લૉગઆઉટ", command=login.initloginpage)
    logout.pack(side='right', anchor=tk.NE, padx=12, pady=10)

    back_button = tk.Button(FSLpage_frame, text="પાછા જાઓ", command=go_back)
    back_button.pack(side='right', anchor=tk.NE, padx=10, pady=10)

    FSLpage_frame.mainloop()

def go_back():
    FSLpage_frame.pack_forget()
    Homepage.open_homepage_r(FSLpage_frame)

def go_home():
    FSLpage_frame.pack_forget()
    Homepage.open_homepage_r(FSLpage_frame)

def fsl_destroyer():
    if FSLpage_frame is not None:
        FSLpage_frame.destroy()
