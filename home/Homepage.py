import tkinter as tk
import MalkhanaTable.MalkhanaPage as mk

def open_homepage():
    
    global hp
    hp = tk.Tk()
    hp.title("HomePage")
    hp.state('zoomed')
    table_button = tk.Button(hp, text="Malkhana Table",command=clicked)
    table_button.pack()
    table_button.pack(pady=20)

    hp.mainloop()

def clicked():
    hp.withdraw()
    mk.mkpage()
    #....


