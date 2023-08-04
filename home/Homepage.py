import tkinter as tk
import login.login as login
import MalkhanaTable.MalkhanaPage as mk
import FSLTable.FSLpage as fp
import Log.log as l
import login.login as lu
import logger
homepage_frame = None

def open_homepage(prev_login_frame):
    prev_login_frame.destroy()
    global homepage_frame
    homepage_destroyer()

    homepage_frame = tk.Frame(prev_login_frame.master)
    homepage_frame.pack()

    FSL_button = tk.Button(homepage_frame, text="એફએસએલ લોગ", command=fsl, font=("Helvetica", 12))
    FSL_button.grid(row=1, column=0,pady=20)
    
    logout = tk.Button(homepage_frame, text="લૉગઆઉટ", command=logoutclicked, font=("Helvetica", 12))
    logout.grid(row=3,pady=20)

    table_button = tk.Button(homepage_frame, text="માલખાના", command=clicked, font=("Helvetica", 12))
    table_button.grid(row=0, column=0,pady=20)

    log_button = tk.Button(homepage_frame, text="લોગ્સ", command=log, font=("Helvetica", 12))
    log_button.grid(row=2, column=0,pady=20)

    homepage_frame.master.title("હોમપેજ")
    homepage_frame.mainloop()

def open_homepage_r(return_frame):
    return_frame.destroy()
    global homepage_frame

    homepage_destroyer()

    homepage_frame = tk.Frame(return_frame.master)
    homepage_frame.pack()

    FSL_button = tk.Button(homepage_frame, text="એફએસએલ લોગ", command=fsl, font=("Helvetica", 12))
    FSL_button.grid(row=1, column=0,pady=20)
    
    logout = tk.Button(homepage_frame, text="લૉગઆઉટ", command=logoutclicked, font=("Helvetica", 12))
    logout.grid(row=3,pady=20)

    table_button = tk.Button(homepage_frame, text="માલખાના", command=clicked, font=("Helvetica", 12))
    table_button.grid(row=0, column=0, pady=20)

    log_button = tk.Button(homepage_frame, text="લોગ્સ", command=log, font=("Helvetica", 12))
    log_button.grid(row=2, column=0,pady=20)

    homepage_frame.master.title("હોમપેજ")

def homepage_destroyer():
    if homepage_frame is not None:
        homepage_frame.destroy()

def logoutclicked():
    logger.log_activity(lu.current_user,"LOG-OUT")
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
