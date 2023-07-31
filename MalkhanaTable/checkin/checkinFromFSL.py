import tkinter as tk
import MalkhanaTable.additems.additems as a
import home.Homepage as Homepage
import MalkhanaTable.checkin.checkinpage as cp
from tkinter import ttk
import sqlite3
from tkcalendar import DateEntry
fsl_checkin_frame = None
def update_item_status(barcode):
    con = sqlite3.connect('databases/items_in_malkhana.db')
    cursor = con.cursor()
    cursor.execute("UPDATE items SET item_status='malkhana' where barcode = ?",(barcode,))
    con.commit()
    con.close()
def checkin():
    
    barcode_no = entry_barcode_no.get()
    checkin_time = f"{hour_var.get()}:{minute_var.get()}"
    checkin_date = entry_checkin_date.get_date()
    examiner = entry_examiner.get()
    examiner_report = text_examiner_report.get("1.0", "end-1c")
    
    update_item_status(barcode_no)
    
    entry_barcode_no.delete(0, tk.END)
    entry_examiner.delete(0, tk.END)
    #entry_checkin_date.set_date("")  # Clear the date entry
    entry_checkin_date.set_date(None)
    text_examiner_report.delete("1.0",tk.END)

def checkin_page(prev_checkin_page):
    global fsl_checkin_frame, entry_barcode_no, entry_checkin_date, hour_var, minute_var, text_examiner_report,entry_examiner
    fsL_checkin_destroyer()
    fsl_checkin_frame = tk.Frame(prev_checkin_page.master)
    fsl_checkin_frame.master.title("Check-in From FSL")

    fsl_checkin_frame.pack(fill=tk.BOTH, expand=True)  # Use pack for the fsl_checkin_frame

    # Labels
    label_barcode_no = ttk.Label(fsl_checkin_frame, text="Barcode No.:")
    label_checkin_time = ttk.Label(fsl_checkin_frame, text="Check-in Time:")
    label_checkin_date = ttk.Label(fsl_checkin_frame, text="Check-in Date:")
    label_examiner = ttk.Label(fsl_checkin_frame, text="Examiner name:")
    label_examiner_report = ttk.Label(fsl_checkin_frame, text="Examiner Report:")

    label_barcode_no.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    label_checkin_time.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    label_checkin_date.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    label_examiner.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
    label_examiner_report.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

    # Entry fields
    entry_barcode_no = ttk.Entry(fsl_checkin_frame)
    entry_barcode_no.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)  # Use sticky=tk.W for left alignment

    hour_var = tk.StringVar(fsl_checkin_frame, value='00')
    minute_var = tk.StringVar(fsl_checkin_frame, value='00')

    hour_menu = ttk.Combobox(fsl_checkin_frame, textvariable=hour_var, values=[str(i).zfill(2) for i in range(24)], state='readonly', width=5)
    minute_menu = ttk.Combobox(fsl_checkin_frame, textvariable=minute_var, values=[str(i).zfill(2) for i in range(60)], state='readonly', width=5)
    hour_menu.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
    minute_menu.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)

    # Date field using tkcalendar
    entry_checkin_date = DateEntry(fsl_checkin_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
    entry_checkin_date.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)  # Use sticky=tk.W for left alignment

  
    entry_examiner = ttk.Entry(fsl_checkin_frame)
    entry_examiner.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

    # Text area for examiner report
    text_examiner_report = tk.Text(fsl_checkin_frame, height=5, width=30)
    text_examiner_report.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)  # Use sticky=tk.W for left alignment

    # Check-in button
    checkin_button = ttk.Button(fsl_checkin_frame, text="Check-in", command=checkin)
    checkin_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10)


    Home = tk.Button(fsl_checkin_frame, text="Home", command=go_home)
    Home.grid(row=6, column=0, padx=10, pady=10, sticky=tk.E)

    back_button = tk.Button(fsl_checkin_frame, text="Back", command=go_back)
    back_button.grid(row=6, column=1, padx=10, pady=10, sticky=tk.W)

def go_home():
    fsL_checkin_destroyer
    Homepage.open_homepage_r(fsl_checkin_frame)

def go_back():
    fsL_checkin_destroyer
    cp.CIpage(fsl_checkin_frame)

def fsL_checkin_destroyer():
    if fsl_checkin_frame is not None:
        fsl_checkin_frame.destroy()