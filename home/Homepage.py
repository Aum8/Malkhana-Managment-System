import tkinter as tk
import login.login as login
import MalkhanaTable.MalkhanaPage as mk
import FSLTable.FSLpage as fp
import Log.log as l
homepage_frame = None

def open_homepage(prev_login_frame):
    prev_login_frame.destroy()
    global homepage_frame
    homepage_destroyer()

    homepage_frame = tk.Frame(prev_login_frame.master)
    homepage_frame.pack()

    table_button = tk.Button(homepage_frame, text="મલખાના ટેબલ", command=clicked)
    table_button.grid(row=0, column=0, pady=20)

    FSL_button = tk.Button(homepage_frame, text="એફએસએલ ટેબલ", command=fsl)
    FSL_button.grid(row=1, column=0, pady=10)

    log_button = tk.Button(homepage_frame, text="Logs", command=log)
    log_button.grid(row=2, column=0, pady=10)

    logout = tk.Button(homepage_frame, text="લૉગઆઉટ", command=logoutclicked)
    logout.grid(row=3, pady=10)

    homepage_frame.master.title("હોમપેજ")
    homepage_frame.mainloop()

def open_homepage_r(return_frame):
    return_frame.destroy()
    global homepage_frame

    homepage_destroyer()

    homepage_frame = tk.Frame(return_frame.master)
    homepage_frame.pack()

    FSL_button = tk.Button(homepage_frame, text="એફએસએલ લોગ", command=fsl)
    FSL_button.grid(row=1, column=0, pady=10)
    
    logout = tk.Button(homepage_frame, text="લૉગઆઉટ", command=logoutclicked)
    logout.grid(row=3, pady=10)

    table_button = tk.Button(homepage_frame, text="મલખાના ટેબલ", command=clicked)
    table_button.grid(row=0, column=0, pady=20)

    log_button = tk.Button(homepage_frame, text="Logs", command=log)
    log_button.grid(row=2, column=0, pady=10)

    homepage_frame.master.title("હોમપેજ")

def homepage_destroyer():
    if homepage_frame is not None:
        homepage_frame.destroy()

def logoutclicked():
    homepage_destroyer()
    login.initloginpage(homepage_frame)

def clicked():
    homepage_destroyer()
    mk.mkpage(homepage_frame)

def fsl():
    homepage_destroyer()
    fp.viewfsl(homepage_frame)

def log():
    homepage_destroyer()
    l.create_logs_page(homepage_frame)
