from tkinter import *
from tkinter import ttk

root = Tk() #Creates a window
root.title ("Julie's Party Rental")
root.iconbitmap('D:\VSCODE\JuliesPartyHire\img\logo.ico')
root.geometry("912x513")
root.configure(bg="#F8F8F9")

#Title
title = Label(root, text="Julie's Party Hire").grid(row = 1, column = 1, sticky= "w")

#Tabs
tabs = ttk.Notebook(root)
tabs.grid(row = 2, column= 1)

registry = Frame(tabs, width = 912, height = 413)
database = Frame(tabs, width = 912, height = 413)

registry.pack(fill="both", expand="1")
database.pack(fill="both", expand="1")

tabs.add(registry, text="Registry")
tabs.add(database, text="Database")

## REGISTRY TAB ##
#Labels and Entry
firstname = Label(registry, text = "First Name:").grid(row = 3, column = 1, sticky = "w")
fn = Entry(registry).grid(row = 4, column = 1)

lastname = Label(registry, text = "Last Name:").grid(row = 3, column = 2, sticky = "w")
ln = Entry(registry).grid(row = 4, column = 2)

recipnum = Label(registry, text = "Recipient Number:").grid(row = 5, column = 1, sticky = "w")
rn = Entry(registry).grid(row = 6, column = 1)

item = Label(registry, text = "Item Hired:") .grid(row = 5, column = 2, sticky = "w")
ih = Entry(registry).grid(row = 6, column = 2)

quanti = Label(registry, text = "Item Quantity:") .grid(row = 7, column = 1, sticky = "w")
iq = Entry(registry).grid(row = 8, column = 1)

#Submit Button
submit = Button(registry, text = "Submit").grid(row = 9, column = 2, sticky = "e")

## DATABASE TAB ##
#Tree View
customertable = ttk.Treeview(database)

#Columns
customertable['columns'] = ("Last Name", "First Name", "Recipient Number", "Item Hired", "Quantity")
customertable.column("#0", width=0, stretch=NO)
customertable.column("Last Name", anchor="w")
customertable.column("First Name", anchor="w")
customertable.column("Recipient Number", anchor="w")
customertable.column("Item Hired", anchor="w")
customertable.column("Quantity", anchor="w")

#Labels
customertable.heading("#0", text="")
customertable.heading("Last Name", text="Last Name")
customertable.heading("First Name", text="First Name")
customertable.heading("Recipient Number", text="Recipient Number")
customertable.heading("Item Hired", text="Item Hired")
customertable.heading("Quantity", text="Quantity")

#Data Insert
data = [

]

count=0
for record in data:
    customertable.insert(parent="", index="end", iid=count, values=(record[0], record[1], record[2], record[3], record[4]))
    count += 1

#Validation


#Append Functions



#Display Table
customertable.grid(column=0,row=0)

root.mainloop()