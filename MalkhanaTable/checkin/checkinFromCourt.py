import tkinter as tk
import MalkhanaTable.additems.additems as a
import home.Homepage as Homepage
import Log.log as log
import MalkhanaTable.checkin.checkinpage as cp
from tkinter import ttk
import sqlite3
from tkcalendar import DateEntry
from tkinter import messagebox
checkin_frame=None
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
    order_details = text_order_details.get("1.0", "end-1c")

    barcode_checker(barcode_no,checkin_date,checkin_time)

    # Clear the input fields after check-in
    entry_barcode_no.delete(0, tk.END)
    entry_checkin_date.set_date(None)  # Clear the date entry
    text_order_details.delete("1.0", tk.END)

def checkin_page_2(root):
    global checkin_frame, entry_barcode_no, entry_checkin_date, hour_var, minute_var, text_order_details
    checkin_frame = tk.Frame(root.master)
    checkin_frame.master.title("Examiner Check-in")

    checkin_frame.pack(fill=tk.BOTH, expand=True)  # Use pack for the checkin_frame

    # Labels
    label_barcode_no = ttk.Label(checkin_frame, text="Barcode No.:")
    label_checkin_time = ttk.Label(checkin_frame, text="Check-in Time:")
    label_checkin_date = ttk.Label(checkin_frame, text="Check-in Date:")
    label_order_details = ttk.Label(checkin_frame, text="Order Details:")

    label_barcode_no.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    label_checkin_time.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    label_checkin_date.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    label_order_details.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

    # Entry fields
    entry_barcode_no = ttk.Entry(checkin_frame)
    entry_barcode_no.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)  # Use sticky=tk.W for left alignment

    hour_var = tk.StringVar(checkin_frame, value='00')
    minute_var = tk.StringVar(checkin_frame, value='00')

    hour_menu = ttk.Combobox(checkin_frame, textvariable=hour_var, values=[str(i).zfill(2) for i in range(24)], state='readonly', width=5)
    minute_menu = ttk.Combobox(checkin_frame, textvariable=minute_var, values=[str(i).zfill(2) for i in range(60)], state='readonly', width=5)
    hour_menu.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
    minute_menu.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)

    # Date field using tkcalendar
    entry_checkin_date = DateEntry(checkin_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
    entry_checkin_date.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)  # Use sticky=tk.W for left alignment

    # Text area for order details
    text_order_details = tk.Text(checkin_frame, height=5, width=30)
    text_order_details.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)  # Use sticky=tk.W for left alignment

    # Check-in button
    checkin_button = ttk.Button(checkin_frame, text="Check-in", command=checkin)
    checkin_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)


    Home = tk.Button(checkin_frame, text="Home", command=go_home)
    Home.grid(row=5, column=0, padx=10, pady=10, sticky=tk.E)

    back_button = tk.Button(checkin_frame, text="Back", command=go_back)
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

def barcode_checker(barcode,date,time):
    conn = sqlite3.connect("databases/items_in_malkhana.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE barcode = ?", (barcode,))
    result = cursor.fetchall()
    conn.close()

    if not result:
        messagebox.showerror("Barcode not found", "The entered barcode does not exist in the database.")
        entry_barcode_no.delete(0, tk.END)
        entry_checkin_date.set_date(None)  # Clear the date entry
        text_order_details.delete("1.0", tk.END)
        return
    already_inornot(barcode,date,time)
    # Clear the input fields after successful checkout
    entry_barcode_no.delete(0, tk.END)
    entry_checkin_date.set_date(None)  # Clear the date entry
    text_order_details.delete("1.0", tk.END)

def already_inornot(barcode,date,time):
    conn = sqlite3.connect("databases/items_in_malkhana.db")
    cursor = conn.cursor()
    cursor.execute("SELECT item_status FROM items WHERE barcode = ?", (barcode,))
    result = cursor.fetchone()
    conn.close()
    if result and result[0] in ("court", "Court"):
        update_item_status(barcode)
        log.update_logs(barcode, "Checked in from Court", date, time)
        messagebox.showinfo("Success", "Item recieved from Court successfully!")
    else:
        messagebox.showerror("Item already available", "The item is already there in Malkhana.")
        entry_barcode_no.delete(0, tk.END)
        entry_checkin_date.set_date(None)  # Clear the date entry
        text_order_details.delete("1.0", tk.END)
