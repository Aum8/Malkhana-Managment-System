import tkinter as tk
import home.Homepage as Homepage
import MalkhanaTable.MalkhanaPage as m

def additems():
    global root
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
    home_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    back_button = tk.Button(root, text="Back", command=go_back)
    back_button.grid(row=8, column=2, columnspan=2, padx=10, pady=10)

    root.mainloop()

def go_back():
    root.destroy()
    m.mkpage()

def go_home(hp):
    root.destroy()
    Homepage.open_homepage()
