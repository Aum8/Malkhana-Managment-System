import login.login as login
import tkinter as tk

def set_custom_theme(root):
    root.tk_setPalette(background="#B9E6FF", foreground="black", activeBackground="#D3D3D3", activeForeground="black")
    root.option_add("*TEntry*background", "white")
    root.option_add("*TEntry*foreground", "black")
    root.option_add("*TEntry*selectBackground", "#B0E0E6")
    root.option_add("*TEntry*selectForeground", "black")
    root.option_add("*TEntry*insertBackground", "black")
    root.option_add("*TButton*background", "white")  # Change the button color to white
    root.option_add("*TButton*foreground", "white")  # Change the button text color to white
    root.option_add("*TButton*activeBackground", "#EBF1F1")  # Slightly lighter blue for active buttons
    root.option_add("*TButton*activeForeground", "white")
    
    # Set a new color for the login button (already set to #EBF1F1 in the original code)
    root.option_add("*TButton.login.TButton*background", "#EBF1F1")  # Light green color for login button

def main():
    root = tk.Tk()
    root.state('zoomed')
    root.title("Main Window")

    # Apply the custom theme
    set_custom_theme(root)
    
    main_frame = tk.Frame(root)
    main_frame.pack()

    login.initloginpage(main_frame)

    root.mainloop()

if __name__ == "__main__":
    main()
