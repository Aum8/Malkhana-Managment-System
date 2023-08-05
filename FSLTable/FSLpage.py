import tkinter as tk
import sqlite3
from tkinter import messagebox
import main
from tkinter import ttk
import home.Homepage as homepage
import MalkhanaTable.MalkhanaPage as m
import login.login as login
import logger as lu
viewfsl_frame = None

def viewfsl(prev_malkhana_frame):
    prev_malkhana_frame.destroy()
    global viewfsl_frame
    fsl_destroyer()
    viewfsl_frame = tk.Frame(prev_malkhana_frame.master)
    viewfsl_frame.master.title("FSL જુઓ")
    viewfsl_frame.pack(fill=tk.BOTH, expand=True)  # To occupy the whole screen

    # Create a Treeview widget to display the data in a tabular format
    tree = ttk.Treeview(viewfsl_frame)

    x_scrollbar = ttk.Scrollbar(tree, orient=tk.HORIZONTAL, command=tree.xview)
    y_scrollbar = ttk.Scrollbar(tree, orient=tk.VERTICAL, command=tree.yview)
    
    # Configure the treeview to use the scrollbars
    tree.configure(xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)
    

    # Define columns
    tree["columns"] = (
        "બારકોડ",
        "FIR નંબર",
        "વસ્તુનું નામ",
        "FSL ઓર્ડર નંબર",
        "ચેકઆઉટ તારીખ",
        "ચેકઆઉટ સમય",
        "લઈ જનાર ઓફિસર ",
        "ચેક ઇન તારીખ",
        "ચેક ઇન સમય",
        "તપાસક નું નામ",
        "FSL રિપોર્ટ"
    )

    # Format columns (adjust the widths as per your requirements)
    tree.column("#0", width=0, stretch=tk.NO)  # Hidden first column
    tree.column("બારકોડ", anchor=tk.W, width=100)
    tree.column("FIR નંબર", anchor=tk.W, width=100)
    tree.column("વસ્તુનું નામ", anchor=tk.W, width=150)
    tree.column("FSL ઓર્ડર નંબર", anchor=tk.W, width=100)
    tree.column("ચેકઆઉટ તારીખ", anchor=tk.W, width=100)
    tree.column("ચેકઆઉટ સમય", anchor=tk.W, width=100)
    tree.column("લઈ જનાર ઓફિસર ", anchor=tk.W, width=150)
    tree.column("ચેક ઇન તારીખ", anchor=tk.W, width=100)
    tree.column("ચેક ઇન સમય", anchor=tk.W, width=100)
    tree.column("તપાસક નું નામ", anchor=tk.W, width=150)
    tree.column("FSL રિપોર્ટ", anchor=tk.W, width=100)

    # Create headings
    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("બારકોડ", text="બારકોડ", anchor=tk.W)
    tree.heading("FIR નંબર", text="FIR નંબર", anchor=tk.W)
    tree.heading("વસ્તુનું નામ", text="વસ્તુનું નામ", anchor=tk.W)
    tree.heading("FSL ઓર્ડર નંબર", text="FSL ઓર્ડર નંબર", anchor=tk.W)
    tree.heading("ચેકઆઉટ તારીખ", text="ચેકઆઉટ તારીખ", anchor=tk.W)
    tree.heading("ચેકઆઉટ સમય", text="ચેકઆઉટ સમય", anchor=tk.W)
    tree.heading("લઈ જનાર ઓફિસર ", text="લઈ જનાર ઓફિસર ", anchor=tk.W)
    tree.heading("ચેક ઇન તારીખ", text="ચેક ઇન તારીખ", anchor=tk.W)
    tree.heading("ચેક ઇન સમય", text="ચેક ઇન સમય", anchor=tk.W)
    tree.heading("તપાસક નું નામ", text="તપાસક નું નામ", anchor=tk.W)
    tree.heading("FSL રિપોર્ટ", text="FSL રિપોર્ટ", anchor=tk.W)

    # Add data to the treeview from the database
    try:
        # Connect to the database (or create if it doesn't exist)
        conn = sqlite3.connect('databases/fsl_records.db')

        # Create a cursor to execute SQL commands
        cursor = conn.cursor()

        # Execute the SQL command to select all rows from the table
        cursor.execute('''SELECT * FROM fsl_records ORDER by timee DESC''')

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

    x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
    y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create a button to go back to the homepage
    back_button = tk.Button(viewfsl_frame, text="પાછા જાઓ", background = "#FFFFFF",command=go_back, font=("Helvetica", 12))
    back_button.pack(pady=10)

    logout = tk.Button(viewfsl_frame, text="લૉગઆઉટ", background = "#FFFFFF", command=logoutclicked, font=("Helvetica", 12))
    logout.pack(padx=12, pady=10)

    # Create a search entry and button
    search_var = tk.StringVar()
    search_entry = tk.Entry(viewfsl_frame, textvariable=search_var)
    search_entry.pack(pady=5)

    # Create a dropdown menu for selecting search field
    search_field_var = tk.StringVar(value="બારકોડ")
    search_field_menu = ttk.Combobox(viewfsl_frame, textvariable=search_field_var, values=tree["columns"], state='readonly')
    search_field_menu.pack()

    search_button = tk.Button(viewfsl_frame, text="શોધ", background = "#FFFFFF", command=lambda: search_fsl(tree, search_field_var.get(), search_var.get()), font=("Helvetica", 12))
    search_button.pack()

    show_all_btn = tk.Button(viewfsl_frame, text="બધા બતાવો",  background = "#FFFFFF",command=lambda: show_all_fsl(tree), font=("Helvetica", 12))
    show_all_btn.pack()

def search_fsl(tree, search_field, search_text):
    # Clear previous search results
    for item in tree.get_children():
        tree.delete(item)

    # Convert the search_field back to the original column name (in English)
    search_field = convert_to_english(search_field)

    # Add data to the treeview from the database based on the search criteria
    try:
        conn = sqlite3.connect('databases/fsl_records.db')
        cursor = conn.cursor()

        cursor.execute(f'''
            SELECT * FROM fsl_records
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

def show_all_fsl(tree):
    for item in tree.get_children():
        tree.delete(item)
    try:
        conn = sqlite3.connect("databases/fsl_records.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM fsl_records ORDER BY timee DESC''')
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
        "FSL ઓર્ડર નંબર": "fsl_order_no",
        "ચેકઆઉટ તારીખ": "checkout_date",
        "ચેકઆઉટ સમય": "checkout_time",
        "કોણ લેવી છે": "taken_by_whom",
        "ચેક ઇન તારીખ": "checkin_date",
        "ચેક ઇન સમય": "checkin_time",
        "તપાસક નું નામ": "examiner_name",
        "FSL રિપોર્ટ": "fsl_report"
    }

    return gujarati_to_english.get(column_name_gujarati, column_name_gujarati)

def fsl_destroyer():
    if viewfsl_frame is not None:
        viewfsl_frame.destroy()
def go_back():
    fsl_destroyer()
    homepage.open_homepage_r(viewfsl_frame)

def go_home():
    fsl_destroyer()
    homepage.open_homepage_r(viewfsl_frame)

def logoutclicked():
    activity = "LOG-OUT"
    lu.log_activity(login.current_user,activity)
    fsl_destroyer()
    login.initloginpage(viewfsl_frame)
  # For testing the viewfsl function
