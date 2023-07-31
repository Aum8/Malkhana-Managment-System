import tkinter as tk
import sqlite3
from tkinter import messagebox
import main
from tkinter import ttk
import home.Homepage as homepage
import MalkhanaTable.MalkhanaPage as m
import login.login as login

viewitems_frame = None

def viewitems(prev_malkhana_frame):
    prev_malkhana_frame.destroy()
    global viewitems_frame
    viewitems_frame = tk.Frame(prev_malkhana_frame.master)
    viewitems_frame.master.title("વસ્તુઓ જુઓ")
    viewitems_frame.pack(fill=tk.BOTH, expand=True)  # To occupy the whole screen

    # Create a Treeview widget to display the data in a tabular format
    tree = ttk.Treeview(viewitems_frame)

    # Define columns
    tree["columns"] = (
        "બારકોડ",
        "FIR નંબર",
        "વસ્તુનું નામ",
        "IPC કલમ",
        "અપરાધ સ્થળ",
        "અપરાધ તારીખ",
        "અપરાધ સમય",
        "અપરાધ સાક્ષીઓ",
        "અપરાધ નિરીક્ષક",
        "વસ્તુનું અવસ્થા",
        "ક્યાં રાખી છે"
    )

    # Format columns
    tree.column("#0", width=0, stretch=tk.NO)  # Hidden first column
    tree.column("બારકોડ", anchor=tk.W, width=100)
    tree.column("FIR નંબર", anchor=tk.W, width=100)
    tree.column("વસ્તુનું નામ", anchor=tk.W, width=150)
    tree.column("IPC કલમ", anchor=tk.W, width=100)
    tree.column("અપરાધ સ્થળ", anchor=tk.W, width=150)
    tree.column("અપરાધ તારીખ", anchor=tk.W, width=100)
    tree.column("અપરાધ સમય", anchor=tk.W, width=100)
    tree.column("અપરાધ સાક્ષીઓ", anchor=tk.W, width=150)
    tree.column("અપરાધ નિરીક્ષક", anchor=tk.W, width=150)
    tree.column("વસ્તુનું અવસ્થા", anchor=tk.W, width=100)
    tree.column("ક્યાં રાખી છે", anchor=tk.W, width=150)

    # Create headings
    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("બારકોડ", text="બારકોડ", anchor=tk.W)
    tree.heading("FIR નંબર", text="FIR નંબર", anchor=tk.W)
    tree.heading("વસ્તુનું નામ", text="વસ્તુનું નામ", anchor=tk.W)
    tree.heading("IPC કલમ", text="IPC કલમ", anchor=tk.W)
    tree.heading("અપરાધ સ્થળ", text="અપરાધ સ્થળ", anchor=tk.W)
    tree.heading("અપરાધ તારીખ", text="અપરાધ તારીખ", anchor=tk.W)
    tree.heading("અપરાધ સમય", text="અપરાધ સમય", anchor=tk.W)
    tree.heading("અપરાધ સાક્ષીઓ", text="અપરાધ સાક્ષીઓ", anchor=tk.W)
    tree.heading("અપરાધ નિરીક્ષક", text="અપરાધ નિરીક્ષક", anchor=tk.W)
    tree.heading("વસ્તુનું અવસ્થા", text="વસ્તુનું અવસ્થા", anchor=tk.W)
    tree.heading("ક્યાં રાખી છે", text="ક્યાં રાખી છે", anchor=tk.W)

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
    back_button = tk.Button(viewitems_frame, text="પાછા જાઓ", command=go_back)
    back_button.pack(pady=10)

    logout = tk.Button(viewitems_frame, text="લૉગઆઉટ", command=logoutclicked)
    logout.pack(padx=12, pady=10)

    # Create a search entry and button
    search_var = tk.StringVar()
    search_entry = tk.Entry(viewitems_frame, textvariable=search_var)
    search_entry.pack(pady=5)

    # Create a dropdown menu for selecting search field
    search_field_var = tk.StringVar(value="બારકોડ")
    search_field_menu = ttk.Combobox(viewitems_frame, textvariable=search_field_var, values=tree["columns"], state='readonly')
    search_field_menu.pack()

    search_button = tk.Button(viewitems_frame, text="શોધ", command=lambda: search_items(tree, search_field_var.get(), search_var.get()))
    search_button.pack()

    show_all_btn = tk.Button(viewitems_frame, text="બધા બતાવો", command=lambda: show_all(tree))
    show_all_btn.pack()

def go_back():
    viewitems_destroyer()
    m.mkpage(viewitems_frame)

def viewitems_destroyer():
    if viewitems_frame is not None:
        viewitems_frame.destroy()
def go_home():
    viewitems_destroyer()
    homepage.open_homepage_r(viewitems_frame)

def logoutclicked():
    viewitems_destroyer()
    login.initloginpage()

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

    # Convert the search_field back to the original column name (in English)
    search_field = convert_to_english(search_field)

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

# Helper function to convert Gujarati column names to English
def convert_to_english(column_name_gujarati):
    # Replace this with the appropriate mapping from Gujarati to English column names
    gujarati_to_english = {
        "બારકોડ": "barcode",
        "FIR નંબર": "fir_number",
        "વસ્તુનું નામ": "item_name",
        "IPC કલમ": "ipc_column",
        "અપરાધ સ્થળ": "crime_location",
        "અપરાધ તારીખ": "crime_date",
        "અપરાધ સમય": "crime_time",
        "અપરાધ સાક્ષીઓ": "crime_witness",
        "અપરાધ નિરીક્ષક": "crime_inspector",
        "વસ્તુનું અવસ્થા": "item_status",
        "ક્યાં રાખી છે": "item_location"
    }

    return gujarati_to_english.get(column_name_gujarati, column_name_gujarati)
