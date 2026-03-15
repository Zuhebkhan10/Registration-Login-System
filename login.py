# Import the tkinter  library
import tkinter as tk
from tkinter import messagebox

# Set up the window
root=tk.Tk()
root.title("Registration Login System")
root.geometry("600x400")
root.config(bg="#f0f2f5")

# Create the center card frame
card=tk.Frame(root,bg="white",width=330,height=280)
card.place(relx=0.5,rely=0.5,anchor="center")

# Create the title
title=tk.Label(card,text="Login",font=("Segoe UI",22,"bold"),bg="white")
title.pack(pady=20)

#Create the username
user_label=tk.Label(card,text="username",bg="white",font=("Segoe UI",10))
user_label.pack()

user_entry=tk.Entry(card,width=50,font=("Segoe UI",11),bd=1)
user_entry.pack(pady=5)

# Create the password
password_label=tk.Label(card,text="Password",bg="WHITE",font=("Segoe UI ",10))
password_label.pack()

password_entry=tk.Entry(card,show="*",width=30,font=("Segoe UI",11),bd=1)
password_entry.pack(pady=5)

# Create the Login function
def login():
    username=user_entry.get()
    password=password_entry.get()
    try:
        with open("users.txt","r")as f:
            users=f.readlines()
    except:
        messagebox.showerror("Error ?","No user registered")
        return
    for user in users:
        u,p=user.strip().split(":")
        if username==u and password==p:
            messagebox.showinfo("Success","Login Successful")
            return
    messagebox.showerror("Error","Invalid Email")

# Create the register function
def register():
    username=user_entry.get()
    password=password_entry.get()

    with open("users.txt","a")as f:
        f.write(username+":"+password + "\n")
    messagebox.showinfo("Success","Account created")

# Create the Buttons
login_btn=tk.Button(card,text="Login",width=20,bg="#4A90E2",fg="white",font=("Segoe UI",10),bd=0,command=login)
login_btn.pack(pady=10)

register_btn=tk.Button(card,text="Register",width=20,bg="#50c878",fg="white",font=("Segoe UI",10),bd=0,command=register)
register_btn.pack()

# Run the Program
root.mainloop()
print(users)
