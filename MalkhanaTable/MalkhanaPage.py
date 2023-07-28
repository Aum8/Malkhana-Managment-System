import tkinter as tk
import home.Homepage as Homepage

def mkpage():
    global root
    root = tk.Toplevel()
    root.title("Malkhana Page")
    root.state('zoomed')

    home_button = tk.Button(root, text="Home", command=go_home)
    home_button.place(x=root.winfo_screenwidth() - 100, y=10, width=80, height=30)


    back_button = tk.Button(root, text="Back", command=go_back)
    back_button.place(x=root.winfo_screenwidth() - 200, y=10, width=80, height=30)
    
    add_button = tk.Button(root, text="Add Items")
    add_button.pack()
    add_button.pack(pady=20)


    view_button = tk.Button(root, text="View Items")
    view_button.pack()
    view_button.pack(pady=20)


    checkin_button = tk.Button(root, text="Check In Items")
    checkin_button.pack()
    checkin_button.pack(pady=20)


    checkout_button = tk.Button(root, text="Check Out Items")
    checkout_button.pack()
    checkout_button.pack(pady=20)

    root.mainloop()

def go_back():
    root.withdraw()
    Homepage.open_homepage()
    

def go_home():
    root.withdraw()
    Homepage.open_homepage()
