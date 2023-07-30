import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry  # Import the DateEntry widget
import home.Homepage as Homepage
import MalkhanaTable.MalkhanaPage as m
import datetime
import login.login as login

def additems(prev_malkhana_frame):
    prev_malkhana_frame.pack_forget()
    global additems_frame
    global barcode_entry, fir_number_entry, item_name_entry, ipc_section_entry, crime_scene_entry, crime_date_entry,crime_witnesses_entry, crime_inspector_entry
    global additems_frame
    global hour_var,minute_var
    additems_frame = tk.Frame(prev_malkhana_frame.master)
    additems_frame.master.title("Add items page")
    additems_frame.pack()

    # Labels
    tk.Label(additems_frame, text="Barcode No:").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(additems_frame, text="FIR No: ").grid(row=1, column=0, padx=10, pady=10)
    tk.Label(additems_frame, text="Item Name:").grid(row=2, column=0, padx=10, pady=10)
    tk.Label(additems_frame, text="IPC Section:").grid(row=3, column=0, padx=10, pady=10)
    tk.Label(additems_frame, text="Crime Scene:").grid(row=4, column=0, padx=10, pady=10)
    tk.Label(additems_frame, text="Crime Date:").grid(row=5, column=0, padx=10, pady=10)
    tk.Label(additems_frame, text="Crime Time:").grid(row=6, column=0, padx=10, pady=10)
    tk.Label(additems_frame, text="Crime Witnesses:").grid(row=7, column=0, padx=10, pady=10)
    tk.Label(additems_frame, text="Crime Inspector:").grid(row=8, column=0, padx=10, pady=10)

    # Entry Fields
    barcode_entry = tk.Entry(additems_frame)
    fir_number_entry = tk.Entry(additems_frame)
    item_name_entry = tk.Entry(additems_frame)
    ipc_section_entry = tk.Entry(additems_frame)
    crime_scene_entry = tk.Entry(additems_frame)
    crime_date_entry = DateEntry(additems_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
    hour_var = tk.StringVar(additems_frame, value='00')
    minute_var = tk.StringVar(additems_frame, value='00')

    hour_menu = ttk.Combobox(additems_frame, textvariable=hour_var, values=[str(i).zfill(2) for i in range(24)], state='readonly', width=5)
    minute_menu = ttk.Combobox(additems_frame, textvariable=minute_var, values=[str(i).zfill(2) for i in range(60)], state='readonly', width=5)
    crime_witnesses_entry = tk.Entry(additems_frame)
    crime_inspector_entry = tk.Entry(additems_frame)

    # Place Entry Fields
    barcode_entry.grid(row=0, column=1, padx=10, pady=10)
    fir_number_entry.grid(row=1,column=1,padx=10,pady=10)
    item_name_entry.grid(row=2, column=1, padx=10, pady=10)
    ipc_section_entry.grid(row=3, column=1, padx=10, pady=10)
    crime_scene_entry.grid(row=4, column=1, padx=10, pady=10)
    crime_date_entry.grid(row=5, column=1, padx=10, pady=10)
    crime_witnesses_entry.grid(row=7, column=1, padx=10, pady=10)
    crime_inspector_entry.grid(row=8, column=1, padx=10, pady=10)
    hour_menu.grid(row=6, column=1, padx=10, pady=10)  # Place the hour drop-down menu
    minute_menu.grid(row=6, column=2, padx=10, pady=10)  # Place the minute drop-down menu


    
    add_item_button = tk.Button(additems_frame, text="Add Item", command=insert_data)
    add_item_button.grid(row=9, column=0, columnspan=4, padx=10, pady=10)

    back_button = tk.Button(additems_frame, text="Back", command=go_back)
    back_button.grid(row=0, column=30, padx=42, pady=10, sticky=tk.SE)

    home_button = tk.Button(additems_frame, text="Home", command= login.initloginpage)
    home_button.grid(row=0, column=32, padx=40, pady=10, sticky=tk.SE)

    logout = tk.Button(additems_frame, text="Logout", command= login.initloginpage)
    logout.grid(row=0, column=34, padx=40, pady=10, sticky=tk.SE)

    

    additems_frame.mainloop()
    return additems_frame, barcode_entry, fir_number_entry, item_name_entry, ipc_section_entry, crime_scene_entry, crime_date_entry, hour_var, minute_var, crime_witnesses_entry, crime_inspector_entry

def insert_data():
    
    global barcode_entry,fir_number_entry,item_name_entry, ipc_section_entry, crime_scene_entry, crime_date_entry, crime_witnesses_entry, crime_inspector_entry
    barcode = barcode_entry.get()
    fir_number = fir_number_entry.get()
    item_name = item_name_entry.get()
    ipc_section = ipc_section_entry.get()
    crime_scene = crime_scene_entry.get()
    crime_date = crime_date_entry.get()
    crime_witnesses = crime_witnesses_entry.get()
    crime_inspector = crime_inspector_entry.get()
    
    crime_hour = int(hour_var.get())
    crime_minute = int(minute_var.get())
    crime_time = f"{crime_hour:02d}:{crime_minute:02d}"


    try:
        # Connect to the database (or create if it doesn't exist)
        conn = sqlite3.connect('databases/items_in_malkhana.db')

        # Create a cursor to execute SQL commands
        cursor = conn.cursor()
       
        cursor.execute('''CREATE TABLE IF NOT EXISTS items (
                            barcode INTEGER PRIMARY KEY AUTOINCREMENT,
                            fir_number TEXT,
                            item_name TEXT,
                            ipc_section TEXT,
                            crime_scene TEXT,
                            crime_date TEXT,
                            crime_time TEXT,
                            crime_witnesses TEXT,
                            crime_inspector TEXT
                        );''')

        # Execute the SQL command to insert data into the table
        cursor.execute('''INSERT INTO items (barcode,fir_number, item_name, ipc_section, 
                          crime_scene, crime_date, crime_time, crime_witnesses, 
                          crime_inspector) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?)''',
                       (barcode,fir_number, item_name, ipc_section, crime_scene, crime_date,
                        crime_time, crime_witnesses, crime_inspector))
        
        # Commit the changes
        conn.commit()
        conn.close()

        # Clear the entry fields
        barcode_entry.delete(0, tk.END)
        fir_number_entry.delete(0, tk.END)
        item_name_entry.delete(0, tk.END)
        ipc_section_entry.delete(0, tk.END)
        crime_scene_entry.delete(0, tk.END)
        crime_date_entry.delete(0, tk.END)
        crime_witnesses_entry.delete(0, tk.END)
        crime_inspector_entry.delete(0, tk.END)

        # Display success message
        messagebox.showinfo("Success", "Item added successfully!")

    except Exception as e:
        # Display error message
        messagebox.showerror("Error", f"Error occurred: {str(e)}")

def go_back():
    additems_frame.pack_forget()
    m.mkpage(additems_frame)

def go_home():
    additems_frame.pack_forget()
    Homepage.open_homepage_r(additems_frame)
