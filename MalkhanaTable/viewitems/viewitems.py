import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter import ttk
import home.Homepage as homepage
import MalkhanaTable.MalkhanaPage as m
import login.login as login

def viewitems(prev_malkhana_frame):
    prev_malkhana_frame.pack_forget()
    global viewitems_frame
    viewitems_frame = tk.Frame(prev_malkhana_frame.master)
    viewitems_frame.master.title("View Items")
    viewitems_frame.pack(fill=tk.BOTH, expand=True)  # To occupy the whole screen

    # Create a Treeview widget to display the data in a tabular format
    tree = ttk.Treeview(viewitems_frame)

    # Define columns
    tree["columns"] = (
        "Barcode",
        "FIR Number",
        "Item Name",
        "IPC Section",
        "Crime Scene",
        "Crime Date",
        "Crime Time",
        "Crime Witnesses",
        "Crime Inspector",
    )

    # Format columns
    tree.column("#0", width=0, stretch=tk.NO)  # Hidden first column
    tree.column("Barcode", anchor=tk.W, width=100)
    tree.column("FIR Number", anchor=tk.W, width=100)
    tree.column("Item Name", anchor=tk.W, width=150)
    tree.column("IPC Section", anchor=tk.W, width=100)
    tree.column("Crime Scene", anchor=tk.W, width=150)
    tree.column("Crime Date", anchor=tk.W, width=100)
    tree.column("Crime Time", anchor=tk.W, width=100)
    tree.column("Crime Witnesses", anchor=tk.W, width=150)
    tree.column("Crime Inspector", anchor=tk.W, width=150)

    # Create headings
    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("Barcode", text="Barcode", anchor=tk.W)
    tree.heading("FIR Number", text="FIR Number", anchor=tk.W)
    tree.heading("Item Name", text="Item Name", anchor=tk.W)
    tree.heading("IPC Section", text="IPC Section", anchor=tk.W)
    tree.heading("Crime Scene", text="Crime Scene", anchor=tk.W)
    tree.heading("Crime Date", text="Crime Date", anchor=tk.W)
    tree.heading("Crime Time", text="Crime Time", anchor=tk.W)
    tree.heading("Crime Witnesses", text="Crime Witnesses", anchor=tk.W)
    tree.heading("Crime Inspector", text="Crime Inspector", anchor=tk.W)

    # Add data to the treeview from the database
    try:
        # Connect to the database (or create if it doesn't exist)
        conn = sqlite3.connect('databases/items_in_malkhana.db')

        # Create a cursor to execute SQL commands
        cursor = conn.cursor()

        # Execute the SQL command to select all rows from the table
        cursor.execute('''SELECT * FROM items''')

        # Fetch all the rows and insert them into the treeview
        for row in cursor.fetchall():
            tree.insert("", tk.END, values=row)

        # Commit the changes
        conn.commit()
        conn.close()

    except Exception as e:
        # Display error message if there's an issue with the database
        tk.messagebox.showerror("Error", f"Error occurred: {str(e)}")

    # Pack the treeview widget with a scrollbar
    tree.pack(fill=tk.BOTH, expand=True)
    scrollbar = tk.Scrollbar(viewitems_frame, orient=tk.VERTICAL, command=tree.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tree.configure(yscrollcommand=scrollbar.set)

    # Create a button to go back to the homepage
    back_button = tk.Button(viewitems_frame, text="Back", command=go_back)
    back_button.pack(pady=10)

    logout = tk.Button(viewitems_frame, text="Logout", command= login.initloginpage)
    logout.pack(padx=12, pady=10)
    # Create a search entry and button
    search_var = tk.StringVar()
    search_entry = tk.Entry(viewitems_frame, textvariable=search_var)
    search_entry.pack(pady=5)

    # Create a dropdown menu for selecting search field
    search_field_var = tk.StringVar(value="Barcode")
    search_field_menu = ttk.Combobox(viewitems_frame, textvariable=search_field_var, values=tree["columns"],state='readonly')
    search_field_menu.pack()

    search_button = tk.Button(viewitems_frame, text="Search", command=lambda: search_items(tree, search_field_var.get(), search_var.get()))
    search_button.pack()

    showall = tk.Button(viewitems_frame, text="Show All", command=lambda: show_all(tree))
    showall.pack()

def go_back():
    viewitems_frame.pack_forget()
    m.mkpage(viewitems_frame)

def go_home():
    viewitems_frame.pack_forget()
    homepage.open_homepage_r(viewitems_frame)

def show_all(tree):
    for item in tree.get_children():
        tree.delete(item)
    try:
        conn = sqlite3.connect("databases/items_in_malkhana.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM items''')
        for row in cursor.fetchall():
            tree.insert("", tk.END, values=row)

        # Commit the changes
        conn.commit()
        conn.close()
    except Exception as e:
        # Display error message if there's an issue with the database
        tk.messagebox.showerror("Error", f"Error occurred: {str(e)}")

def search_items(tree, search_field, search_text):
    # Clear previous search results
    for item in tree.get_children():
        tree.delete(item)

    search_field = search_field.lower().replace(" ", "_")
    # Add data to the treeview from the database based on the search criteria
    try:
        conn = sqlite3.connect('databases/items_in_malkhana.db')
        cursor = conn.cursor()

        cursor.execute(f'''
            SELECT * FROM items
            WHERE {search_field} LIKE ?
        ''', ('%' + search_text + '%',))

        # Fetch the rows and insert them into the treeview
        for row in cursor.fetchall():
            tree.insert("", tk.END, values=row)

        # Commit the changes
        conn.commit()
        conn.close()

    except Exception as e:
        # Display error message if there's an issue with the database
        tk.messagebox.showerror("Error", f"Error occurred: {str(e)}")
