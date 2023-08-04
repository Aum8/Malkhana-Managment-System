import tkinter as tk
import MalkhanaTable.additems.additems as a
import home.Homepage as Homepage
import MalkhanaTable.checkin.checkinpage as cp
import Log.log as log
from tkinter import messagebox
from tkinter import ttk
import sqlite3
from tkcalendar import DateEntry
import logger as lu
import login.login as login

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
    order_no = entry_order_no.get()
    examiner = entry_examiner.get()
    examiner_report = text_examiner_report.get("1.0", "end-1c")
    
    barcode_checker(barcode_no, checkin_date, checkin_time, order_no, examiner, examiner_report)

def checkin_page(prev_checkin_page):
    global fsl_checkin_frame, entry_barcode_no, entry_order_no, entry_checkin_date, hour_var, minute_var, text_examiner_report, entry_examiner
    fsL_checkin_destroyer()
    fsl_checkin_frame = tk.Frame(prev_checkin_page.master)
    fsl_checkin_frame.master.title("FSLથી ચેક-ઇન")

    fsl_checkin_frame.pack(fill=tk.BOTH, expand=True)  # Use pack for the fsl_checkin_frame

    # Labels
    label_barcode_no = ttk.Label(fsl_checkin_frame, text="બારકોડ નંબર:", background="#B9E6FF", font=("Helvetica", 12))
    label_order_no = ttk.Label(fsl_checkin_frame, text="ઓર્ડર નંબર:",  background="#B9E6FF",font=("Helvetica", 12))
    label_checkin_time = ttk.Label(fsl_checkin_frame, text="ચેક-ઇન સમય:", background="#B9E6FF", font=("Helvetica", 12))
    label_checkin_date = ttk.Label(fsl_checkin_frame, text="ચેક-ઇન તારીખ:", background="#B9E6FF", font=("Helvetica", 12))
    label_examiner = ttk.Label(fsl_checkin_frame, text="પરીક્ષકનું નામ:",  background="#B9E6FF",font=("Helvetica", 12))
    label_examiner_report = ttk.Label(fsl_checkin_frame, text="પરીક્ષક રિપોર્ટ:",  background="#B9E6FF",font=("Helvetica", 12))

    label_barcode_no.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    label_order_no.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    label_checkin_time.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    label_checkin_date.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
    label_examiner.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
    label_examiner_report.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

    # Entry fields
    entry_barcode_no = ttk.Entry(fsl_checkin_frame, font=("Helvetica", 12))
    entry_barcode_no.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)  # Use sticky=tk.W for left alignment
    entry_order_no = ttk.Entry(fsl_checkin_frame, font=("Helvetica", 12))
    entry_order_no.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

    hour_var = tk.StringVar(fsl_checkin_frame, value='00')
    minute_var = tk.StringVar(fsl_checkin_frame, value='00')

    hour_menu = ttk.Combobox(fsl_checkin_frame, textvariable=hour_var, values=[str(i).zfill(2) for i in range(24)], state='readonly', width=5)
    minute_menu = ttk.Combobox(fsl_checkin_frame, textvariable=minute_var, values=[str(i).zfill(2) for i in range(60)], state='readonly', width=5)
    hour_menu.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky=tk.W)
    minute_menu.grid(row=2, column=3, columnspan=2, padx=5, pady=5, sticky=tk.W)


    # Date field using tkcalendar
    entry_checkin_date = DateEntry(fsl_checkin_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
    entry_checkin_date.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)  # Use sticky=tk.W for left alignment

    entry_examiner = ttk.Entry(fsl_checkin_frame,  background="#FFFFFF",font=("Helvetica", 12))
    entry_examiner.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

    # Text area for examiner report
    text_examiner_report = tk.Text(fsl_checkin_frame, height=5, background="#FFFFFF", width=30, font=("Helvetica", 12))
    text_examiner_report.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)  # Use sticky=tk.W for left alignment

    # Check-in button
    checkin_button = tk.Button(fsl_checkin_frame, text="ચેક-ઇન", background="#FFFFFF", command=checkin, font=("Helvetica", 12))
    checkin_button.grid(row=6, column=0, columnspan=2, padx=5, pady=10)

    Home = tk.Button(fsl_checkin_frame, text="હોમપેજ",  background="#FFFFFF",command=go_home, font=("Helvetica", 12))
    Home.grid(row=7, column=0, padx=10, pady=10, sticky=tk.E)

    back_button = tk.Button(fsl_checkin_frame, text="પાછા જાઓ",  background="#FFFFFF",command=go_back, font=("Helvetica", 12))
    back_button.grid(row=7, column=1, padx=10, pady=10, sticky=tk.W)

def go_home():
    fsL_checkin_destroyer()
    Homepage.open_homepage_r(fsl_checkin_frame)

def go_back():
    fsL_checkin_destroyer()
    cp.CIpage(fsl_checkin_frame)

def fsL_checkin_destroyer():
    if fsl_checkin_frame is not None:
        fsl_checkin_frame.destroy()


def barcode_checker(barcode,date,time,order_no,examiner,examiner_report):
    conn = sqlite3.connect("databases/items_in_malkhana.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE barcode = ?", (barcode,))
    result = cursor.fetchall()
    conn.close()

    if not result:
        messagebox.showerror("બારકોડ મળ્યો નથી", "દાખલ કરેલો બારકોડ ડેટાબેઝમાં અસ્તિત્વમાં નથી.")
        # Clear the input fields after showing the error
        entry_barcode_no.delete(0, tk.END)
        entry_examiner.delete(0, tk.END)
        entry_checkin_date.set_date(None)
        text_examiner_report.delete("1.0",tk.END)
        return
    already_inornot(barcode,date,time,order_no,examiner,examiner_report)
    # Clear the input fields after successful checkout
    entry_barcode_no.delete(0, tk.END)
    entry_examiner.delete(0, tk.END)
    entry_checkin_date.set_date(None)
    text_examiner_report.delete("1.0",tk.END)

def already_inornot(barcode,date,time,order_no,examiner,examiner_report):
    conn = sqlite3.connect("databases/items_in_malkhana.db")
    cursor = conn.cursor()
    cursor.execute("SELECT item_status FROM items WHERE barcode = ?", (barcode,))
    result = cursor.fetchone()
    conn.close()
    if result and result[0] in ("fsl", "FSL"):
        update_item_status(barcode)
        log.update_logs(barcode, "FSLથી ચેક-ઇન", date, time)
        messagebox.showinfo("સફળતા", "મુદ્દામાલ સફળતાપૂર્વક FSL માંથી મળ્યું છે!")
        updatefsl(barcode,date,time,order_no,examiner,examiner_report)
        activity = "Item checked in from FSL barcode no:"+barcode
        lu.log_activity(login.current_user,activity)
        
    else:
        messagebox.showerror("મુદ્દામાલ પહેલેથીજ ઉપલબ્ધ છે", "આ મુદ્દામાલ માલખાનામાં પહેલેથીજ ઉપલબ્ધ છે.")
        entry_barcode_no.delete(0, tk.END)
        entry_examiner.delete(0, tk.END)
        entry_checkin_date.set_date(None)
        text_examiner_report.delete("1.0",tk.END)

def updatefsl(barcode,date,time,order_no,examiner,examiner_report):
    conn = sqlite3.connect("databases/fsl_records.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE fsl_records SET checkin_date = ?,checkin_time=?,examiner_name=?,fsl_report = ? WHERE fsl_order_no = ?",(date,time,examiner,examiner_report,order_no))
    entry_barcode_no.delete(0, tk.END)
    entry_examiner.delete(0, tk.END)
    entry_checkin_date.set_date(None)
    text_examiner_report.delete("1.0",tk.END)
    conn.commit()
    conn.close()
