import tkinter as tk
import sqlite3
from tkinter import ttk, messagebox
from database import create_db

#creates db on first launch. If not, then it skips
create_db()

#functions
def search_db_all():
    conn = sqlite3.connect("BIM.db")
    c = conn.cursor()
    devices = c.execute("SELECT *, oid FROM BIM")
    return devices

def search_db_barcode():
    code1 = searchentry.get()
    conn = sqlite3.connect("BIM.db")
    c = conn.cursor()
    devices = c.execute(f"SELECT *, oid FROM BIM WHERE code = '{code1}'")
    return devices

def butten_search():
    my_tree.delete(*my_tree.get_children())
    for d in search_db_barcode():
        my_tree.insert(parent="", index="end", iid=d[5], text="", values=(d[0], d[1], d[2], d[3], d[4]))
    searchentry.delete(0, tk.END)

def refresh_view():
    my_tree.delete(*my_tree.get_children())
    for d in search_db_all():
        my_tree.insert(parent="", index="end", iid=d[5], text="", values=(d[0], d[1], d[2], d[3], d[4]))




#root window basics
root = tk.Tk()
root.geometry("1200x400")
root.title("Bart's Inventory Management System")


#creating frame/tree and packing items together
frame = tk.Frame(root)


my_tree = ttk.Treeview(frame)

my_tree["columns"] = ("code", "device_type", "serial", "location", "label_printed")

my_tree.column("#0", width=0, stretch="no")
my_tree.column("code", anchor="w", minwidth=25,  width=120)
my_tree.column("device_type", anchor="w", minwidth=25,  width=120)
my_tree.column("serial", anchor="w", minwidth=25,  width=120 )
my_tree.column("location", anchor="w", minwidth=25,  width=120 )
my_tree.column("label_printed", anchor="w", minwidth=10,  width=120 )

my_tree.heading("#0", text="", anchor="w")
my_tree.heading("code", text="code", anchor="w")
my_tree.heading("device_type", text="device_type", anchor="w")
my_tree.heading("serial", text="serial", anchor="w")
my_tree.heading("location", text="location", anchor="w")
my_tree.heading("label_printed", text="label_printed", anchor="w")


refresh_view()





searchbtn = tk.Button(frame, text="Search", command=butten_search)
searchlabel = tk.Label(frame, text="Search by Barcode")
searchentry = tk.Entry(frame)
refreshbtn = tk.Button(frame, text="Refresh", command=refresh_view)


my_tree.pack()
searchlabel.pack()
searchentry.pack()
searchbtn.pack()
refreshbtn.pack()
frame.pack()


root.mainloop()