import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import datetime, date
CL_frame=None
# def fetch_logs():
#     # Fetch logs data from the SQLite database
#     conn = sqlite3.connect('malkhana.db')
#     cursor = conn.cursor()

#     cursor.execute("SELECT * FROM logs")
#     logs_data = cursor.fetchall()

#     conn.close()
#     return logs_data

def search_logs(search_barcode):
    # Fetch logs data from the SQLite database based on the search barcode
    conn = sqlite3.connect('malkhana.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM logs WHERE Barcode=?", (search_barcode,))
    logs_data = cursor.fetchall()

    conn.close()
    return logs_data

# def search_and_display_logs(search_barcode, logs_tree):
    # if not search_barcode:
    #     logs_data = fetch_logs()
    # else:
    #     logs_data = search_logs(search_barcode)

    # logs_tree.delete(*logs_tree.get_children())

    # for log_entry in logs_data:
    #     logs_tree.insert("", tk.END, values=log_entry)

def create_logs_page(prev_homepage_frame):
    prev_homepage_frame.destroy()
    global CL_frame
    create_logs_page_destroyer()
    CL_frame = tk.Frame(prev_homepage_frame.master)
    CL_frame.master.title("Logs")
    CL_frame.pack()

    logs_tree_frame = ttk.Frame(CL_frame)
    logs_tree_frame.pack(fill=tk.BOTH, expand=True)

    logs_tree_scroll = ttk.Scrollbar(logs_tree_frame)
    logs_tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

    logs_tree = ttk.Treeview(
        logs_tree_frame,
        columns=("Barcode", "Status", "Date", "Time"),
        show="headings",
        yscrollcommand=logs_tree_scroll.set
    )
    logs_tree.pack(fill=tk.BOTH, expand=True)

    logs_tree_scroll.config(command=logs_tree.yview)

    logs_tree.heading("Barcode", text="Barcode")
    logs_tree.heading("Status", text="Check-in/Check-out")
    logs_tree.heading("Date", text="Date")
    logs_tree.heading("Time", text="Time")

    logs_tree.column("Barcode", width=150, anchor=tk.CENTER)
    logs_tree.column("Status", width=150, anchor=tk.CENTER)
    logs_tree.column("Date", width=100, anchor=tk.CENTER)
    logs_tree.column("Time", width=100, anchor=tk.CENTER)

    # logs_data = fetch_logs()

    # for log_entry in logs_data:
    #     logs_tree.insert("", tk.END, values=log_entry)

    search_frame = ttk.Frame(CL_frame)
    search_frame.pack(pady=10)

    barcode_search_label = ttk.Label(search_frame, text="Search by Barcode:")
    barcode_search_label.pack(side=tk.LEFT)

    barcode_search_entry = ttk.Entry(search_frame, width=20)
    barcode_search_entry.pack(side=tk.LEFT, padx=5)

    search_button = ttk.Button(search_frame, text="Search",)
                            #    command=lambda: '''search_and_display_logs(barcode_search_entry.get(),''' logs_tree))
    search_button.pack(side=tk.LEFT)

    CL_frame.mainloop()


def create_logs_page_destroyer():
    if CL_frame is not None:
        CL_frame.destroy()