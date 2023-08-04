import tkinter as tk
from tkinter import ttk
import home.Homepage as Homepage
import MalkhanaTable.checkin.checkinpage as cp
import sqlite3
from datetime import datetime, date

CL_frame = None

def update_logs(barcode, status, date, time):
    conn = sqlite3.connect('databases/logs.db')
    cursor = conn.cursor()
    # Create the 'logs' table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS logs (
                        Barcode TEXT,
                        Status TEXT,
                        Date DATE,
                        Time TEXT
                    )''')
    # Assuming that the 'logs' table has columns: "Barcode", "Status", "Date", "Time"
    cursor.execute("INSERT INTO logs (Barcode, Status, Date, Time) VALUES (?, ?, ?, ?)",
                   (barcode, status, date, time))

    conn.commit()
    conn.close()

def search_logs(search_barcode):
    # Fetch logs data from the SQLite database based on the search barcode
    conn = sqlite3.connect('databases/logs.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM logs WHERE Barcode=?", (search_barcode,))
    logs_data = cursor.fetchall()

    conn.close()
    return logs_data
def create_logs_page(prev_homepage_frame):
    prev_homepage_frame.destroy()
    global CL_frame
    CL_destroyer()
    CL_frame = tk.Frame(prev_homepage_frame.master)
    CL_frame.master.title("લોગ્સ")
    CL_frame.pack()

    logs_tree_frame = ttk.Frame(CL_frame)
    logs_tree_frame.pack(fill=tk.BOTH, expand=True)

    logs_tree_scroll = ttk.Scrollbar(logs_tree_frame)
    logs_tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

    logs_tree = ttk.Treeview(
        logs_tree_frame,
        columns=("Barcode", "Status", "Date", "Time"),
        show="headings",
        yscrollcommand=logs_tree_scroll.set,
        height=30
    )
    logs_tree.pack(fill=tk.BOTH, expand=True)

    logs_tree_scroll.config(command=logs_tree.yview)

    logs_tree.heading("Barcode", text="બારકોડ")
    logs_tree.heading("Status", text="ચેક-ઇન/ચેક-આઉટ")
    logs_tree.heading("Date", text="તારીખ")
    logs_tree.heading("Time", text="સમય")

    logs_tree.column("Barcode", width=250, anchor=tk.CENTER)
    logs_tree.column("Status", width=250, anchor=tk.CENTER)
    logs_tree.column("Date", width=200, anchor=tk.CENTER)
    logs_tree.column("Time", width=200, anchor=tk.CENTER)

    search_frame = ttk.Frame(CL_frame)
    search_frame.pack(pady=10, anchor=tk.S)  # Align to the bottom of CL_frame

    barcode_search_label = ttk.Label(search_frame, background="#B9E6FF", text="બારકોડ દ્વારા શોધો:", font=("Helvetica", 12))
    barcode_search_label.pack(side=tk.LEFT)

    barcode_search_entry = ttk.Entry(search_frame,  background="#B9E6FF",width=20, font=("Helvetica", 12))
    barcode_search_entry.pack(side=tk.LEFT, padx=5)

    search_button = tk.Button(search_frame, background="#FFFFFF", text="શોધ", command=lambda: search_logs_and_display(barcode_search_entry.get(), logs_tree), font=("Helvetica", 12))
    search_button.pack(side=tk.LEFT)

    Home = tk.Button(CL_frame, text="હોમપેજ",  background="#FFFFFF",command=go_home, font=("Helvetica", 12))
    Home.pack(side=tk.LEFT, padx=10, pady=10)

    CL_frame.mainloop()

def search_logs_and_display(search_barcode, logs_tree):
    logs_data = search_logs(search_barcode)
    logs_tree.delete(*logs_tree.get_children())

    for log_entry in logs_data:
        logs_tree.insert("", tk.END, values=log_entry)


def go_home():
    CL_destroyer()
    Homepage.open_homepage_r(CL_frame)

def CL_destroyer():
    if CL_frame is not None:
        CL_frame.destroy()
