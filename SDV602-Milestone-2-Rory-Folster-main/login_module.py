from tkinter import messagebox
import tkinter as tk
import sqlite3
import highest_crime_module
import datetime
import global_functions
import pyodbc

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'Server=RORYS-PC;'
                      'Database=Users;'
                      'UID=remote_connection;'
                      'PWD=123;')

def login():
    # Testing login
    # rory
    # Rorukz123

    # getting form data
    global uname
    uname = username.get()
    pwd = password.get()
    # applying empty validation
    if uname == "" or pwd == "":
        messagebox.showinfo("Empty fields", "Fields cannot be empty")
    else:
        # open database
        # select query
        cursor = conn.execute(
            "SELECT * from users where USERNAME='%s' and PASS='%s'" % (uname, pwd)
        )
        # fetch data
        if cursor.fetchone():
            messagebox.showinfo("Login success", "Login sucess")
            conn.execute("UPDATE users SET is_online = 1 WHERE USERNAME='%s'" % uname)
            conn.commit()
            global_functions.current_user.append(uname)
            login_screen.withdraw()
            highest_crime_module.highest_crime_areas()
            print(f"{uname} logged in successfully.")
            with open("logs.txt", "a+") as text_file:
                text_file.write(f"{datetime.datetime.now()}: {uname} logged into the server.\n")
        else:
            messagebox.showinfo("Wrong credentials", "Incorrect username or password.")


def register():
    uname = username.get()
    pwd = password.get()
    # applying empty validation
    if uname == "" or pwd == "":
        messagebox.showinfo("Empty fields", "Fields cannot be empty")
    else:
        # select query
        conn.execute(
            "INSERT INTO users(USERNAME, PASS, is_online) VALUES('%s', '%s', 0)" % (uname, pwd)
        )
        # commit querry
        conn.commit()
        messagebox.showinfo("Account created", "Account created. Welcome to the application.")
        conn.close()
        login_screen.withdraw()
        highest_crime_module.highest_crime_areas()
        print(f"{datetime.datetime.now()}: {uname} has created an account and logged in. ")
        with open("logs.txt", "a+") as text_file:
            text_file.write(f"{datetime.datetime.now()}: {uname} has created an account and logged in.\n")


def loginScreen():
    global login_screen
    login_screen = tk.Tk()
    login_screen.geometry("350x250+100+100")

    global username
    global password
    username = tk.StringVar()
    password = tk.StringVar()

    tk.Label(login_screen, width="300", text="Login Form").pack()
    tk.Label(login_screen, text="Username: ").place(x=20, y=40)
    tk.Entry(login_screen, textvariable=username).place(
        x=120, y=42
    )  # Adding textvariable so i can grab the data in login function
    tk.Label(login_screen, text="Password: ").place(x=20, y=80)
    tk.Entry(login_screen, textvariable=password, show="*").place(
        x=120, y=82
    )  # Making password input display as * to imporve security.
        #Adding textvariable so i can grab the data for login function
    tk.Button(
        login_screen,
        text="Login",
        width=10,
        height=1,
        command=login,
        bg="#0E6655",
        fg="white",
        font=("Arial", 12, "bold"),
    ).place(x=125, y=170)
    tk.Button(
        login_screen,
        text="Register",
        width=10,
        height=1,
        command=register,
        bg="#0E6655",
        fg="white",
        font=("Arial", 12, "bold"),
    ).place(x=125, y=210)

    # login_screen.protocol("WM_DELETE_WINDOW", highest_crime_module.on_closing)
    login_screen.mainloop()