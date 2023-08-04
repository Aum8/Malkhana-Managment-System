import login.login as login
import tkinter as tk
current_user =None
def main():
    root = tk.Tk()
    root.state('zoomed')
    root.title("Main Window")

    main_frame = tk.Frame(root)
    main_frame.pack()

    login.initloginpage(main_frame)

    root.mainloop()

if __name__ == "__main__":
    main()  
