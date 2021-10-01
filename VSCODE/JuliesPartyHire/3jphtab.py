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

registry = Frame(tabs)
database = Frame(tabs)

registry.pack(fill="both", expand="1")
database.pack(fill="both", expand="1")

tabs.add(registry, text="Registry")
tabs.add(database, text="Database")

#Labels and Entry
firstname = Label(registry, text="First Name:").grid(row = 3, column = 1, sticky = "w")
fn = Entry(registry).grid(row = 4, column = 1)

lastname = Label(registry, text="Last Name:").grid(row = 3, column = 2, sticky = "w")
ln = Entry(registry).grid(row = 4, column = 2)

recepnum = Label(registry, text="Recipient Number:").grid(row = 5, column = 1, sticky = "w")
rn = Entry(registry).grid(row = 6, column = 1)

item = Label(registry, text="Item Hired:") .grid(row = 5, column = 2, sticky = "w")
ih = Entry(registry).grid(row = 6, column = 2)

quanti = Label(registry, text="Item Quantity:") .grid(row = 7, column = 1, sticky = "w")
iq = Entry(registry).grid(row = 8, column = 1)

#Submit Button
submit = Button(registry, text="Submit").grid(row = 9, column = 2, sticky = "e")

root.mainloop()