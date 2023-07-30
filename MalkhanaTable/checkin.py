import tkinter as tk
from tkinter import ttk
import MalkhanaTable.MalkhanaPage as m
import home.Homepage as homepage

def checkinPage(prev_malkhana_frame):
    prev_malkhana_frame.pack_forget()
    global checkin_frame, entry_widgets,frame,tree
    checkin_frame = tk.Frame(prev_malkhana_frame.master)
    checkin_frame.master.title("Check-In Page")
    checkin_frame.pack(fill=tk.BOTH, expand=True)  # To occupy the whole screen

    # Create a frame to hold the entry widgets and buttons
    frame = ttk.Frame(checkin_frame, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Create labels and entry widgets for each field
    labels = ["FIR No.", "Check-in Time", "IPC Section", "Submitting Officer", "Forensic Examiner", "Description of Evidence",
            "Chain of Custody", "Examination Details", "Start Date of Examination", "End Date of Examination", "Final Report"]

    entry_widgets = []
    for i, label_text in enumerate(labels):
        label = ttk.Label(frame, text=label_text)
        label.grid(row=i, column=0, sticky=tk.W, padx=5, pady=5)

        entry = ttk.Entry(frame, width=40)
        entry.grid(row=i, column=1, sticky=tk.W, padx=5, pady=5)
        entry_widgets.append(entry)

    # Create a treeview to display the records
    columns = labels
    tree = ttk.Treeview(frame, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)
    tree.grid(row=len(labels)+1, column=0, columnspan=2, padx=5, pady=5)

    # Create an "Add Record" button
    checkin_button = ttk.Button(frame, text="Check-In", command=lambda: add_checkin_record(tree, entry_widgets))
    checkin_button.grid(row=len(labels)+2, column=0, columnspan=2, padx=5, pady=5)

    # Function to add the check-in record to the treeview
def add_checkin_record(tree, entry_widgets):
    # Get values from the entry widgets
    fir_no = entry_widgets[0].get()
    check_in_time = entry_widgets[1].get()
    ipc_section = entry_widgets[2].get()
    submitting_officer = entry_widgets[3].get()
    forensic_examiner = entry_widgets[4].get()
    description_of_evidence = entry_widgets[5].get()
    chain_of_custody = entry_widgets[6].get()
    examination_details = entry_widgets[7].get()
    start_date = entry_widgets[8].get()
    end_date = entry_widgets[9].get()
    final_report = entry_widgets[10].get()

    # Add the values to the treeview
    tree.insert("", "end", values=(fir_no, check_in_time, ipc_section, submitting_officer, forensic_examiner,
                                    description_of_evidence, chain_of_custody, examination_details, start_date,
                                    end_date, final_report))

    # Clear the entry widgets after adding the record
    clear_entries()

# Function to clear the entry widgets
def clear_entries():
    for entry in entry_widgets:
        entry.delete(0, tk.END)


def go_back():
    checkin_frame.pack_forget()
    m.mkpage(checkin_frame)

def go_home():
    checkin_frame.pack_forget()
    homepage.open_homepage_r(checkin_frame)
