import tkinter as tk
import MalkhanaTable.additems.additems as a
import home.Homepage as Homepage
import Log.log as log
import MalkhanaTable.checkin.checkinpage as cp
from tkinter import ttk
import sqlite3
from tkcalendar import DateEntry
from tkinter import messagebox

checkin_frame = None

def update_item_status(barcode):
    conn = sqlite3.connect('databases/items_in_malkhana.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE items SET item_status='માળખાના' where barcode = ?", (barcode,))
    conn.commit()
    conn.close()

def checkin():
    barcode_no = entry_barcode_no.get()
    checkin_time = f"{hour_var.get()}:{minute_var.get()}"
    checkin_date = entry_checkin_date.get_date()
    order_details = text_order_details.get("1.0", "end-1c")

    barcode_checker(barcode_no, checkin_date, checkin_time)

    # Clear the input fields after check-in
    entry_barcode_no.delete(0, tk.END)
    entry_checkin_date.set_date(None)  # Clear the date entry
    text_order_details.delete("1.0", tk.END)

def checkin_page_2(root):
    global checkin_frame, entry_barcode_no, entry_checkin_date, hour_var, minute_var, text_order_details
    checkin_frame = tk.Frame(root.master)
    checkin_frame.master.title("પરીક્ષક ચેક-ઇન")

    checkin_frame.pack(fill=tk.BOTH, expand=True)  # Use pack for the checkin_frame

    # Labels
    label_barcode_no = ttk.Label(checkin_frame, text="બારકોડ નંબર:", font=("Helvetica", 12))
    label_checkin_time = ttk.Label(checkin_frame, text="ચેક-ઇન સમય:", font=("Helvetica", 12))
    label_checkin_date = ttk.Label(checkin_frame, text="ચેક-ઇન તારીખ:", font=("Helvetica", 12))
    label_order_details = ttk.Label(checkin_frame, text="ઓર્ડરની વિગતો:", font=("Helvetica", 12))

    label_barcode_no.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    label_checkin_time.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    label_checkin_date.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    label_order_details.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

    # Entry fields
    entry_barcode_no = ttk.Entry(checkin_frame, font=("Helvetica", 12))
    entry_barcode_no.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)  # Use sticky=tk.W for left alignment

    hour_var = tk.StringVar(checkin_frame, value='00')
    minute_var = tk.StringVar(checkin_frame, value='00')

    hour_menu = ttk.Combobox(checkin_frame, textvariable=hour_var, values=[str(i).zfill(2) for i in range(24)],
                             state='readonly', width=5)
    minute_menu = ttk.Combobox(checkin_frame, textvariable=minute_var, values=[str(i).zfill(2) for i in range(60)],
                               state='readonly', width=5)
    hour_menu.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
    minute_menu.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)

    # Date field using tkcalendar
    entry_checkin_date = DateEntry(checkin_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
    entry_checkin_date.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)  # Use sticky=tk.W for left alignment

    # Text area for order details
    text_order_details = tk.Text(checkin_frame, height=5, width=30, font=("Helvetica", 12))
    text_order_details.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)  # Use sticky=tk.W for left alignment

    # Check-in button
    checkin_button = tk.Button(checkin_frame, text="ચેક-ઇન", command=checkin, font=("Helvetica", 12))
    checkin_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

    Home = tk.Button(checkin_frame, text="હોમપેજ", command=go_home, font=("Helvetica", 12))
    Home.grid(row=5, column=0, padx=10, pady=10, sticky=tk.E)

    back_button = tk.Button(checkin_frame, text="પાછા જાઓ", command=go_back, font=("Helvetica", 12))
    back_button.grid(row=5, column=1, padx=10, pady=10, sticky=tk.W)

def go_home():
    checkin_destroyer()
    Homepage.open_homepage_r(checkin_frame)

def go_back():
    checkin_destroyer()
    cp.CIpage(checkin_frame)

def checkin_destroyer():
    if checkin_frame is not None:
        checkin_frame.destroy()

def barcode_checker(barcode, date, time):
    conn = sqlite3.connect("databases/items_in_malkhana.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE barcode = ?", (barcode,))
    result = cursor.fetchall()
    conn.close()

    if not result:
        messagebox.showerror("બારકોડ મળ્યો નથી", "દાખલ કરેલો બારકોડ ડેટાબેઝમાં અસ્તિત્વમાં નથી.")
        entry_barcode_no.delete(0, tk.END)
        entry_checkin_date.set_date(None)  # Clear the date entry
        text_order_details.delete("1.0", tk.END)
        return
    already_in_or_not(barcode, date, time)
    # Clear the input fields after successful checkout
    entry_barcode_no.delete(0, tk.END)
    entry_checkin_date.set_date(None)  # Clear the date entry
    text_order_details.delete("1.0", tk.END)

def already_in_or_not(barcode, date, time):
    conn = sqlite3.connect("databases/items_in_malkhana.db")
    cursor = conn.cursor()
    cursor.execute("SELECT item_status FROM items WHERE barcode = ?", (barcode,))
    result = cursor.fetchone()
    conn.close()
    if result and result[0] in ("court", "Court"):
        update_item_status(barcode)
        log.update_logs(barcode, "કોર્ટમાંથી ચેક-ઇન", date, time)
        messagebox.showinfo("સફળતા", "આઇટમ સફળતાથી માળખાનામાં પ્રાપ્ત કરવામાં આવ્યો છે!")
    else:
        messagebox.showerror("આઇટમ પહેલેથીજ માળખાનામાં છે", "આઇટમ પહેલેથીજ માળખાનામાં છે.")
        entry_barcode_no.delete(0, tk.END)
        entry_checkin_date.set_date(None)  # Clear the date entry
        text_order_details.delete("1.0", tk.END)
