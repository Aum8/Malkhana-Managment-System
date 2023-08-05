import tkinter as tk
import sqlite3
from tkinter import messagebox
import home.Homepage as Homepage
import pandas as pd
import os
#
print_frame = None

def printPage(prev_malkhana_frame):
    prev_malkhana_frame.destroy()
    global print_frame
    print_frame = tk.Frame(prev_malkhana_frame.master)
    print_frame.master.title("Print Details")
    print_frame.pack(fill=tk.BOTH, expand=True)  # To occupy the whole screen
    
    search_label = tk.Label(print_frame, text="બારકોડ:",font=("Helvetica", 24))
    search_label.pack(pady=50)
    
    search_entry = tk.Entry(print_frame,  background="#FFFFFF")
    search_entry.pack(pady=5)
    
    print_button = tk.Button(print_frame, text="પ્રિન્ટ",  background="#FFFFFF", font=("Helvetica", 12), command=lambda: print_details(search_entry.get()))
    print_button.pack(pady=20)

    Home = tk.Button(print_frame, text="હોમપેજ",  background="#FFFFFF",command=go_home, font=("Helvetica", 12))
    Home.pack(pady=5)

    print_frame.mainloop()
#
def print_details(barcode=None):
    # Connect to the database and retrieve data
    try:
        if os.path.exists('exported_data.xlsx'):
            os.remove('exported_data.xlsx')
        conn = sqlite3.connect('databases/items_in_malkhana.db')

        if barcode is None:
            query = "SELECT * FROM items"
        else:
            query = "SELECT barcode,fir_number,	item_name,ipc_section,crime_scene,crime_date,crime_time	,crime_witnesses,crime_inspector,item_status,where_its_kept,timee FROM items WHERE barcode = ?"

        query_string = f"{query}"

        df = pd.read_sql_query(query_string, conn, params=(barcode,))
        conn.close()

        with pd.ExcelWriter('exported_data.xlsx', mode='w') as writer:
            df.to_excel(writer, sheet_name='Malkhana Table', index=False)

        conn = sqlite3.connect('databases/fsl_records.db')

        if barcode is None:
            query = "SELECT * FROM fsl_records"
        else:
            query = "SELECT * FROM fsl_records WHERE barcode = ?"

        query_string = f"{query}"

        df = pd.read_sql_query(query_string, conn, params=(barcode,))
        conn.close()

        with pd.ExcelWriter('exported_data.xlsx', mode='a') as writer:
            df.to_excel(writer, sheet_name='FSL Table', index=False)

        conn = sqlite3.connect('databases/logs.db')

        if barcode is None:
            query = "SELECT * FROM logs"
        else:
            query = "SELECT * FROM logs WHERE barcode = ?"

        query_string = f"{query}"

        df = pd.read_sql_query(query_string, conn, params=(barcode,))
        conn.close()

        with pd.ExcelWriter('exported_data.xlsx', mode='a') as writer:
            df.to_excel(writer, sheet_name='Logs', index=False)
        messagebox.showinfo("Success", "Data exported to Excel successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def go_home():
    CL_destroyer()
    Homepage.open_homepage_r(print_frame)
def CL_destroyer():
    if print_frame is not None:
        print_frame.destroy()