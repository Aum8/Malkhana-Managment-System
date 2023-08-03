import login.login as login
import tkinter as tk
def main():
    root = tk.Tk()
    root.state('zoomed')
    root.title("Main Window")
    root.configure(bg='#263238')
    main_frame = tk.Frame(root)
    main_frame.pack()

    login.initloginpage(main_frame)

    root.mainloop()

if __name__ == "__main__":
    main()  
