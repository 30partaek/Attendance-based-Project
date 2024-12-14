import tkinter as tk
from tkinter import messagebox
import mysql.connector
import subprocess
from PIL import Image,ImageTk


# Connect to MySQL database
mydb = mysql.connector.connect(
     host="localhost",
     user="root",
     password="partaek2171014@",
    database="login"
)

mycursor = mydb.cursor()

def register(username, password):
    try:
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        val = (username, password)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Registration Successful", "User registered successfully")
        return True
    except mysql.connector.Error as err:
        messagebox.showerror("Registration Failed", f"Error: {err}")
        return False

def authenticate(username, password):
    try:
        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        val = (username, password)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        if result:
            return True
        else:
            return False
    except mysql.connector.Error as err:
        messagebox.showerror("Authentication Error", f"Error: {err}")
        return False

def login():
    username = username_entry.get()
    password = password_entry.get()

    if authenticate(username, password):
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        open_facerecognition()
        root.destroy()  # Close the login window
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def open_facerecognition():
    subprocess.Popen(["python", "main.py"])

def register_user():
    username = username_entry.get()
    password = password_entry.get()

    if register(username, password):
        clear_entries()

def clear_entries():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Login")

# Username Label and Entry
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

# Password Label and Entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Login Button
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, padx=10, pady=10)

# Register Button
register_button = tk.Button(root, text="Register", command=register_user)
register_button.grid(row=2, column=1, padx=10, pady=10)





root.mainloop()
