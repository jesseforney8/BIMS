import tkinter as tk
import psycopg2
from tkinter import ttk, messagebox, Toplevel
from database import create_db, db_command

#creates db on first launch. If not, then it skips
create_db()

#functions
global counter
counter = 0

def open_add_window():
    global counter
    if counter < 1:
        global window2
        window2 = Toplevel(root)
        window2.title("Add Entry")
        window2.geometry("1200x400")
        counter +=1
        window2.protocol("WM_DELETE_WINDOW", on_closing_add)

        code_label = tk.Label(window2, text="Code").pack()
        code_entry = tk.Entry(window2).pack()
        device_type = tk.Label(window2, text="Device Type").pack()
        device_type_entry = tk.Entry(window2).pack()
        serial_label = tk.Label(window2, text="Serial").pack()
        serial_entry = tk.Entry(window2).pack()
        location_label = tk.Label(window2, text="Location").pack()
        location_entry = tk.Entry(window2).pack()
        label_printed_label = tk.Label(window2, text="Label Printed?").pack()
        label_printed_entry = tk.Entry(window2).pack()
        submit_add_btn = tk.Button(window2, text="Add").pack()
        
    
def on_closing_add():
    window2.destroy()
    global counter
    counter-= 1
            

def open_modify_window():
    global counter
    if counter < 1:
        global window3
        window3 = Toplevel(root)
        window3.title("Modify Entry")
        window3.geometry("1200x400")
        counter +=1
        window3.protocol("WM_DELETE_WINDOW", on_closing_modify)

        

def on_closing_modify():
    window3.destroy()
    global counter
    counter-= 1








#root window basics

root = tk.Tk()
root.geometry("1200x400")
root.title("Bart's Inventory Management System")

#configure global columns

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)

#creating frames
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)

#frame1 basics labels
label_connected_to = tk.Label(frame1, text="Connected to...")
label_table = tk.Label(frame1, text="test")

label_connected_to.grid()
label_table.grid()

#frame2 treeview
my_tree = ttk.Treeview(frame2)

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

my_tree.grid()




#frame3 buttons

pad_x = 20
pad_y = 5

add_btn = tk.Button(frame3, text="Add", padx=pad_x, command=open_add_window)
modify_btn = tk.Button(frame3, text="Modify", padx=pad_x, command=open_modify_window)
refresh_btn = tk.Button(frame3, text="Refresh", padx=pad_x)
search_btn = tk.Button(frame3, text="Search", padx=pad_x)


add_btn.grid(column=0, row=0, padx=pad_x, pady=pad_y)
modify_btn.grid(column=1, row=0, padx=pad_x, pady=pad_y)
refresh_btn.grid(column=2, row=0, padx=pad_x, pady=pad_y)
search_btn.grid(column=3, row=0, padx=pad_x, pady=pad_y)




#add frames

frame1.grid(column=2)
frame2.grid(column=2)
frame3.grid(column=2)



#show screen



root.mainloop()