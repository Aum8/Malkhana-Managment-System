import tkinter as tk
import home.Homepage as Homepage
import MalkhanaTable.checkout.checkoutpage as cof
import MalkhanaTable.MalkhanaPage as m
from tkinter import ttk
import sqlite3
from tkcalendar import DateEntry

checkout_frame = None
def update_item_status(barcode):
    con = sqlite3.connect('databases/items_in_malkhana.db')
    cursor = con.cursor()
    cursor.execute("UPDATE items SET item_status='FSL' where barcode = ?",(barcode,))
    con.commit()
    con.close()

def checkout_destroyer():
    if checkout_frame is not None:
        checkout_frame.destroy()

def checkouttoFSL(root):
    root.destroy()
    barcode = entry_barcode.get()
    fir_no = entry_fir_no.get()
    item_name = entry_item_name.get()
    taken_by_whom = entry_taken_by_whom.get()
    date = entry_checkout_date.get_date()
    time = f"{hour_var.get()}:{minute_var.get()}"
    order_no = entry_order_no.get()

    update_item_status(entry_barcode)

    # Clear the input fields after checkout
    entry_barcode.delete(0, tk.END)
    entry_fir_no.delete(0, tk.END)
    entry_item_name.delete(0, tk.END)
    entry_taken_by_whom.delete(0, tk.END)
    entry_checkout_date.set_date("")  # Clear the date entry
    order_no.delete(0 , tk.END)

def checkouttoFSL_page(root):
    root.destroy()
    global checkout_frame, entry_barcode, entry_fir_no, entry_item_name, entry_taken_by_whom, entry_checkout_date, hour_var, minute_var,entry_order_no
    checkout_destroyer()
    checkout_frame = tk.Frame(root.master)
    checkout_frame.master.title("Checkout to FSL")
    checkout_frame.pack()

    # Labels
    label_barcode = ttk.Label(checkout_frame, text="Barcode:")
    label_fir_no = ttk.Label(checkout_frame, text="FIR No.:")
    label_item_name = ttk.Label(checkout_frame, text="Item Name:")
    label_taken_by_whom = ttk.Label(checkout_frame, text="Taken by Whom:")
    label_checkout_date = ttk.Label(checkout_frame, text="Checkout Date:")
    label_checkout_time = ttk.Label(checkout_frame, text="Checkout Time:")
    label_order_no =ttk.Label(checkout_frame, text="Order No.:")

    label_barcode.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    label_fir_no.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    label_item_name.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    label_taken_by_whom.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
    label_checkout_date.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)
    label_checkout_time.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
    label_order_no.grid(row=4,column=0,padx=5,pady=5,sticky=tk.W)

    # Entry fields
    entry_barcode = ttk.Entry(checkout_frame)
    entry_fir_no = ttk.Entry(checkout_frame)
    entry_item_name = ttk.Entry(checkout_frame)
    entry_taken_by_whom = ttk.Entry(checkout_frame)
    entry_order_no = ttk.Entry(checkout_frame)
    entry_nature_of_case = ttk.Entry(checkout_frame)
    entry_barcode.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
    entry_fir_no.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
    entry_item_name.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
    entry_taken_by_whom.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
    entry_order_no.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)
    
    hour_var = tk.StringVar(checkout_frame, value='00')
    minute_var = tk.StringVar(checkout_frame, value='00')

    hour_menu = ttk.Combobox(checkout_frame, textvariable=hour_var, values=[str(i).zfill(2) for i in range(24)], state='readonly', width=5)
    minute_menu = ttk.Combobox(checkout_frame, textvariable=minute_var, values=[str(i).zfill(2) for i in range(60)], state='readonly', width=5)
    hour_menu.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)
    minute_menu.grid(row=6, column=2, padx=5, pady=5, sticky=tk.W)

    # Date field using tkcalendar
    entry_checkout_date = DateEntry(checkout_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
    entry_checkout_date.grid(row=7, column=1, padx=5, pady=5, sticky=tk.W)

    # Checkout button
    checkout_button = ttk.Button(checkout_frame, text="Checkout to FSL", command=checkouttoFSL)
    checkout_button.grid(row=8, column=0, columnspan=2, padx=5, pady=10)

    # Home and Back buttons
    home_button = tk.Button(checkout_frame, text="Home", command=go_home)
    home_button.grid(row=9, column=0, padx=10, pady=10, sticky=tk.E)

    back_button = tk.Button(checkout_frame, text="Back", command=go_back)
    back_button.grid(row=9, column=1, padx=10, pady=10, sticky=tk.W)

def go_back():
    checkout_destroyer()
    m.mkpage(checkout_frame)

    

def go_home():
    checkout_destroyer()
    Homepage.open_homepage_r(checkout_frame)