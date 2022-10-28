"""
Module to contain generic functions that I can call on each DES.
"""

from tkinter import messagebox
import login_module
import client_module
import datetime
import pyodbc

current_user = []

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'Server=RORYS-PC;'
                      'Database=Users;'
                      'UID=remote_connection;'
                      'PWD=123;')
        conn.execute("UPDATE users SET is_online = 0 WHERE USERNAME='%s'" % current_user[0])
        conn.commit()
        with open("logs.txt", "a+") as text_file:
            text_file.write(f"{datetime.datetime.now()}: {current_user[0]} logged out.\n")
        login_module.login_screen.destroy()


def open_chat():
    client_module.chat_room_window()