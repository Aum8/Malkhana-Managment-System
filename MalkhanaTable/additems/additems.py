import tkinter as tk
import home.Homepage as Homepage
import MalkhanaTable.MalkhanaPage as m
import sqlite3
import tkinter.messagebox as messagebox

def additems():
    global root
    global barcode_entry, item_name_entry, ipc_section_entry, crime_scene_entry, crime_date_entry, crime_time_entry, crime_witnesses_entry, crime_inspector_entry
    root = tk.Toplevel()
    root.title("Add items")
    root.state('zoomed')

    # Labels
    tk.Label(root, text="Barcode No:").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(root, text="Item Name:").grid(row=1, column=0, padx=10, pady=10)
    tk.Label(root, text="IPC Section:").grid(row=2, column=0, padx=10, pady=10)
    tk.Label(root, text="Crime Scene:").grid(row=3, column=0, padx=10, pady=10)
    tk.Label(root, text="Crime Date:").grid(row=4, column=0, padx=10, pady=10)
    tk.Label(root, text="Crime Time:").grid(row=5, column=0, padx=10, pady=10)
    tk.Label(root, text="Crime Witnesses:").grid(row=6, column=0, padx=10, pady=10)
    tk.Label(root, text="Crime Inspector:").grid(row=7, column=0, padx=10, pady=10)

    # Entry Fields
    barcode_entry = tk.Entry(root)
    item_name_entry = tk.Entry(root)
    ipc_section_entry = tk.Entry(root)
    crime_scene_entry = tk.Entry(root)
    crime_date_entry = tk.Entry(root)
    crime_time_entry = tk.Entry(root)
    crime_witnesses_entry = tk.Entry(root)
    crime_inspector_entry = tk.Entry(root)

    # Place Entry Fields
    barcode_entry.grid(row=0, column=1, padx=10, pady=10)
    item_name_entry.grid(row=1, column=1, padx=10, pady=10)
    ipc_section_entry.grid(row=2, column=1, padx=10, pady=10)
    crime_scene_entry.grid(row=3, column=1, padx=10, pady=10)
    crime_date_entry.grid(row=4, column=1, padx=10, pady=10)
    crime_time_entry.grid(row=5, column=1, padx=10, pady=10)
    crime_witnesses_entry.grid(row=6, column=1, padx=10, pady=10)
    crime_inspector_entry.grid(row=7, column=1, padx=10, pady=10)

    home_button = tk.Button(root, text="Home", command=go_home)
    home_button.place(x=root.winfo_screenwidth() - 100, y=10, width=80, height=30)


    back_button = tk.Button(root, text="Back", command=go_back)
    back_button.place(x=root.winfo_screenwidth() - 200, y=10, width=80, height=30)

    add_item_button = tk.Button(root, text="Add Item", command=insert_data)
    add_item_button.grid(row=8, column=0, columnspan=4, padx=10, pady=10)

    root.mainloop()
    return root, barcode_entry, item_name_entry, ipc_section_entry, crime_scene_entry, crime_date_entry, crime_time_entry, crime_witnesses_entry, crime_inspector_entry

def insert_data():
    # Retrieve data from the entry fields
    global barcode_entry, item_name_entry, ipc_section_entry, crime_scene_entry, crime_date_entry, crime_time_entry, crime_witnesses_entry, crime_inspector_entry
    barcode = barcode_entry.get()
    item_name = item_name_entry.get()
    ipc_section = ipc_section_entry.get()
    crime_scene = crime_scene_entry.get()
    crime_date = crime_date_entry.get()
    crime_time = crime_time_entry.get()
    crime_witnesses = crime_witnesses_entry.get()
    crime_inspector = crime_inspector_entry.get()
    

    try:
        # Connect to the database (or create if it doesn't exist)
        conn = sqlite3.connect('databases/my_database.db')

        # Create a cursor to execute SQL commands
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS items (
                            barcode INTEGER PRIMARY KEY AUTOINCREMENT,
                            item_name TEXT,
                            ipc_section TEXT,
                            crime_scene TEXT,
                            crime_date TEXT,
                            crime_time TEXT,
                            crime_witnesses TEXT,
                            crime_inspector TEXT
                        );''')

        # Execute the SQL command to insert data into the table
        cursor.execute('''INSERT INTO items (barcode, item_name, ipc_section, 
                          crime_scene, crime_date, crime_time, crime_witnesses, 
                          crime_inspector) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                       (barcode, item_name, ipc_section, crime_scene, crime_date,
                        crime_time, crime_witnesses, crime_inspector))

        # Commit the changes
        conn.commit()
        conn.close()

        # Clear the entry fields
        barcode_entry.delete(0, tk.END)
        item_name_entry.delete(0, tk.END)
        ipc_section_entry.delete(0, tk.END)
        crime_scene_entry.delete(0, tk.END)
        crime_date_entry.delete(0, tk.END)
        crime_time_entry.delete(0, tk.END)
        crime_witnesses_entry.delete(0, tk.END)
        crime_inspector_entry.delete(0, tk.END)

        # Display success message
        messagebox.showinfo("Success", "Item added successfully!")

    except Exception as e:
        # Display error message
        messagebox.showerror("Error", f"Error occurred: {str(e)}")

def go_back():
    root.destroy()
    m.mkpage()

def go_home(hp):
    root.destroy()
    Homepage.open_homepage()
