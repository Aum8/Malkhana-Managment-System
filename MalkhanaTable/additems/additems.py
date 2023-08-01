import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry  
import home.Homepage as Homepage
import MalkhanaTable.MalkhanaPage as m
import login.login as login
import datetime
additems_frame = None
def additems(prev_malkhana_frame):
    prev_malkhana_frame.destroy()

    global additems_frame
    global barcode_entry, fir_number_entry, item_name_entry, ipc_section_entry, crime_scene_entry, crime_date_entry,hour_var,minute_var,crime_witnesses_entry, crime_inspector_entry,item_status_entry,where_its_kept_entry
    additems_destroyer()
    additems_frame = tk.Frame(prev_malkhana_frame.master)
    additems_frame.master.title("વસ્તુઓ ઉમેરો")
    additems_frame.pack()

    # Labels
    tk.Label(additems_frame, text="બારકોડ નંબર:").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(additems_frame, text="FIR નંબર: ").grid(row=1, column=0, padx=10, pady=10)
    tk.Label(additems_frame, text="જબ્ત વસ્તુઓ:").grid(row=2, column=0, padx=10, pady=10)
    tk.Label(additems_frame, text="IPC કલમ:").grid(row=3, column=0, padx=10, pady=10)
    tk.Label(additems_frame, text="અપરાધ સ્થળ:").grid(row=4, column=0, padx=10, pady=10)
    tk.Label(additems_frame, text="અપરાધ તારીખ:").grid(row=5, column=0, padx=10, pady=10)
    tk.Label(additems_frame, text="અપરાધ સમય:").grid(row=6, column=0, padx=10, pady=10)
    tk.Label(additems_frame, text="અપરાધ સાક્ષીઓ:").grid(row=7, column=0, padx=10, pady=10)
    tk.Label(additems_frame, text="અપરાધ નિરીક્ષક:").grid(row=8, column=0, padx=10, pady=10)
    tk.Label(additems_frame, text="વસ્તુની સ્થિતિ:").grid(row=9, column=0, padx=10, pady=10)
    tk.Label(additems_frame, text="ક્યાં સંગ્રહિત છે:").grid(row=10, column=0, padx=10, pady=10)    

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
    item_status_entry = tk.Entry(additems_frame)
    where_its_kept_entry = tk.Entry(additems_frame)

    # Place Entry Fields
    barcode_entry.grid(row=0, column=1, padx=10, pady=10)
    fir_number_entry.grid(row=1,column=1,padx=10,pady=10)
    item_name_entry.grid(row=2, column=1, padx=10, pady=10)
    ipc_section_entry.grid(row=3, column=1, padx=10, pady=10)
    crime_scene_entry.grid(row=4, column=1, padx=10, pady=10)
    crime_date_entry.grid(row=5, column=1, padx=10, pady=10)
    crime_witnesses_entry.grid(row=7, column=1, padx=10, pady=10)
    crime_inspector_entry.grid(row=8, column=1, padx=10, pady=10)
    item_status_entry.grid(row=9, column=1, padx=10, pady=10)
    where_its_kept_entry.grid(row=10, column=1, padx=10, pady=10)
    hour_menu.grid(row=6, column=1, padx=10, pady=10)  # Place the hour drop-down menu
    minute_menu.grid(row=6, column=2, padx=10, pady=10)  # Place the minute drop-down menu


    
    add_item_button = tk.Button(additems_frame, text="આઇટમ ઉમેરો", command=insert_data)
    add_item_button.grid(row=13, column=0, columnspan=4, padx=10, pady=10)

    back_button = tk.Button(additems_frame, text="પાછા જાઓ", command=go_back)
    back_button.grid(row=0, column=30, padx=42, pady=10, sticky=tk.SE)

    home_button = tk.Button(additems_frame, text="હોમ", command=go_home)
    home_button.grid(row=0, column=32, padx=40, pady=10, sticky=tk.SE)

    logout = tk.Button(additems_frame, text="લૉગઆઉટ", command=logoutclicked)
    logout.grid(row=0, column=34, padx=40, pady=10, sticky=tk.SE)


    
    additems_frame.mainloop()
    
def insert_data():
    
    global barcode_entry,fir_number_entry,item_name_entry, ipc_section_entry, crime_scene_entry, crime_date_entry, crime_witnesses_entry, crime_inspector_entry,item_status_entry,where_its_kept_entry
    barcode = barcode_entry.get()
    fir_number = fir_number_entry.get()
    item_name = item_name_entry.get()
    ipc_section = ipc_section_entry.get()
    crime_scene = crime_scene_entry.get()
    crime_date = crime_date_entry.get()
    crime_witnesses = crime_witnesses_entry.get()
    crime_inspector = crime_inspector_entry.get()
    item_status = item_status_entry.get()
    where_its_kept = where_its_kept_entry.get()
    
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
                            crime_inspector TEXT,
                            item_status TEXT,
                            where_its_kept TEXT,
                            timee TEXT
                        );''')
        timee = datetime.datetime.now()
        # Execute the SQL command to insert data into the table
        cursor.execute('''INSERT INTO items (barcode,fir_number, item_name, ipc_section, 
                          crime_scene, crime_date, crime_time, crime_witnesses, 
                          crime_inspector,item_status,where_its_kept,timee) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?,?,?,?)''',
                       (barcode,fir_number, item_name, ipc_section, crime_scene, crime_date,
                        crime_time, crime_witnesses, crime_inspector,item_status,where_its_kept,timee))
        
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
        item_status_entry.delete(0, tk.END)
        where_its_kept_entry.delete(0, tk.END)




        messagebox.showinfo("Success", "Item added successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {str(e)}")

def go_back():
    additems_destroyer()
    m.mkpage(additems_frame)

def go_home():
    additems_destroyer()
    Homepage.open_homepage_r(additems_frame)

def logoutclicked():
    additems_destroyer()
    login.initloginpage(additems_frame)

def additems_destroyer():
    if additems_frame is not None:
        additems_frame.destroy()