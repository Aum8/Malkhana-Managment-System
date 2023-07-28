# Import functions and modules from the subfolders
import login.login as login
import home.Homepage as Homepage
import login.logindb as logindb


def main():
    # Call the login page function from login.py
    login.initloginpage()

if __name__ == "__main__":
    main()

