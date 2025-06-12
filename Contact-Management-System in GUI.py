import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox
import ttkbootstrap as tb
import mysql.connector as mc
from tkinter.constants import *
from MySQLDB import add_contact,update_contact,delete_contact,get_all_contacts

self = tb.Window(themename="pulse")
self.title("Contact Management System")
self.geometry("600x550")
self.maxsize(700,650)
self.iconbitmap("D:\Prodigy InfoTech\Task 3\phone.ico")
 
lbl1 = tb.Label(self,text="Contact Management System",font=("Times New Roman",18,"bold"),bootstyle="Primary")
lbl1.pack(padx=5,pady=5,side="top")

f1 = tb.Frame(self)
f1.pack(padx=5,pady=5)

lbl2 = tb.Label(f1,text="Name")
lbl2.pack(pady=5,padx=5,side="left")

e1 = tb.Entry(f1,text="")
e1.pack(pady=5,padx=5,side="left")

f2 = tb.Frame(self)
f2.pack(padx=5,pady=5)

lbl3 = tb.Label(f2,text="Phone")
lbl3.pack(pady=5,padx=5,side="left")

e2 = tb.Entry(f2,text="")
e2.pack(pady=5,padx=5,side="left")

f3 = tb.Frame(self)
f3.pack(pady=5,padx=5)

lbl4 = tb.Label(f3,text="Email")
lbl4.pack(padx=5,pady=5,side="left")

e3 = tb.Entry(f3,text="")
e3.pack(padx=5,pady=5,side="left")
def submit_info():
    name = e1.get()
    phone = e2.get()
    email = e3.get()
    if not(name and phone and email):
        messagebox.showerror("Error", "Please fill all fields")
   

    if add_contact(name, phone, email):
        messagebox.showinfo("Successfully", "Information Inserted Successfully")
    else:
        messagebox.showerror("Error", "Failed to insert information")
    
f4 = tb.Frame(self)
f4.pack(padx=5,pady=5)

btn1 = tb.Button(f4,text="Submit",bootstyle="Primary",command=submit_info)
btn1.pack(padx=5,pady=5)

def open_contact_window():
    top = tb.Toplevel(title="All Contacts")
    top.geometry("700x500")
    top.iconbitmap(r"D:\Prodigy InfoTech\Task 3\add-user.ico")

    # --- Treeview Setup ---
    columns = ("ID", "Name", "Phone", "Email")
    tree = tb.Treeview(top, columns=columns, show="headings", bootstyle="info")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    tree.pack(padx=10, pady=10, fill=BOTH, expand=True)

    # --- Input Fields for Update ---
    entry_frame = tb.Frame(top)
    entry_frame.pack(pady=10)

    name_var = tb.StringVar()
    phone_var = tb.StringVar()
    email_var = tb.StringVar()

    tb.Entry(entry_frame, textvariable=name_var, width=20).grid(row=0, column=0, padx=5)
    tb.Entry(entry_frame, textvariable=phone_var, width=20).grid(row=0, column=1, padx=5)
    tb.Entry(entry_frame, textvariable=email_var, width=25).grid(row=0, column=2, padx=5)

    # --- Button Actions ---
    def refresh():
        for item in tree.get_children():
            tree.delete(item)
        for row in get_all_contacts():
            tree.insert("", "end", iid=row[0], values=row)

    def on_select(event):
        selected = tree.focus()
        if selected:
            values = tree.item(selected, 'values')
            name_var.set(values[1])
            phone_var.set(values[2])
            email_var.set(values[3])

    def delete_selected():
        selected = tree.focus()
        if selected:
            delete_contact(selected)
            refresh()

    def update_selected():
        selected = tree.focus()
        if selected:
            update_contact(selected, name_var.get(), phone_var.get(), email_var.get())
            refresh()
    def go_back():
        refresh()
        top.destroy()

    # --- Buttons ---
    btn_frame = tb.Frame(top)
    btn_frame.pack(pady=10)

    tb.Button(btn_frame, text="Update", command=update_selected, bootstyle="warning").pack(side=LEFT, padx=10)
    tb.Button(btn_frame, text="Delete", command=delete_selected, bootstyle="danger").pack(side=LEFT, padx=10)
    tb.Button(btn_frame, text="Refresh", command=refresh, bootstyle="success").pack(side=LEFT, padx=10)
    tb.Button(btn_frame, text="Back",command=go_back).pack(side=LEFT,padx=10)
    tree.bind("<<TreeviewSelect>>", on_select)

    # Load initial data
    refresh()

tb.Button(self, text="View Contacts", command=open_contact_window, bootstyle="primary").pack(pady=40)

tb.Label(self,text="Developed By Muhammad Yasir With 💖").pack(side=BOTTOM,padx=10,pady=20)






self.mainloop()
