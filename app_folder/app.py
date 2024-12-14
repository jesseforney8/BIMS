import tkinter as tk
import psycopg2
from tkinter import ttk, messagebox
from database import create_db

#creates db on first launch. If not, then it skips
create_db()

#functions




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







searchbtn = tk.Button(frame, text="Search")
searchlabel = tk.Label(frame, text="Search by Barcode")
searchentry = tk.Entry(frame)
refreshbtn = tk.Button(frame, text="Refresh")


my_tree.pack()
searchlabel.pack()
searchentry.pack()
searchbtn.pack()
refreshbtn.pack()
frame.pack()


root.mainloop()