from tkinter import *
from tkinter import ttk

root = Tk() #Creates a window
root.title ("Julie's Party Rental")
root.iconbitmap('D:\VSCODE\JuliesPartyHire\img\logo.ico')
root.geometry("912x513")
root.configure(bg="#F8F8F9")

#Validation
def validate ():
    incorrectinput = 0

    #First Name Correct
    if len(fn.get()) > 0 and len(fn.get()) <= 200:
        firstname.config(text="First Name:", fg="black")

    #First Name Incorrect
    if len(fn.get()) == 0:
        firstname.config(text="First Name: Missing", fg="pink")
        incorrectinput = 1
    if len(fn.get()) > 200:
        firstname.config(text="First Name: 200 Character Limit", fg="pink")
        incorrectinput = 1


    #Last Name Correct
    if len(ln.get()) > 0 and len(ln.get()) <= 200:
        lastname.config(text = "Last Name:", fg="black")

    #Last Name Incorrect
    if len(ln.get()) == 0 or len(ln.get()) > 200:
        lastname.config(text = "Last Name: Missing", fg="pink")
        incorrectinput = 1
    if len(ln.get()) > 200:
        lastname.config(text = "Last Name: 200 Character Limit", fg="pink")
        incorrectinput = 1
    

    #Recipient Number
    if (rn.get().isdigit()):
        #Recipient Number Correct
        if int(rn.get()) > 0 or int(rn.get()) <= 500:
            recipnum.config(text="Recipient Number:", fg="black")
        #Recipient Number Incorrect
        if int(rn.get()) <= 0:
            recipnum.config(text="#Recipient Number: Missing", fg="pink")
            incorrectinput = 1
        
    else:
        recipnum.config(text="Item Quantity: Missing", fg="pink")
        incorrectinput = 1

    #Item Hired Correct
    if len(ih.get()) > 0 and len(ih.get()) <= 50:
        item.config(text="Item Hired:", fg="black")

    #Item Hired Incorrect
    if len(ih.get()) == 0 :
        item.config(text="Item Hired: Missing", fg="pink")
        incorrectinput = 1
    if len(ih.get()) > 50 :
        item.config(text = "Item Hired: 50 Character Limit", fg="pink")
        incorrectinput = 1
    

    #Item Quantity
    if (iq.get().isdigit()):
        #Item Quantity Correct
        if int(iq.get()) > 0 or int(iq.get()) <= 500:
            quanti.config(text="Item Quantity:", fg="black")
        #Item Quantity Incorrect
        if int(iq.get()) <= 0 or int(iq.get()) > 500:
            quanti.config(text="Item Quantity: 1 - 500", fg="pink")
            incorrectinput = 1
        
    else:
        quanti.config(text="Item Quantity: Missing", fg="pink")
        incorrectinput = 1

    if incorrectinput == 0 :
        append()

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
firstname = Label(registry, text = "First Name:")
firstname.grid(row = 3, column = 1, sticky = "w")
fn = Entry(registry)
fn.grid(row=4, column=1, sticky="w")

lastname = Label(registry, text="Last Name:")
lastname.grid(row=3, column=2, sticky="w")
ln = Entry(registry)
ln.grid(row=4, column=2, stick ="w")

recipnum = Label(registry, text="Recipient Number:")
recipnum.grid(row=5, column=1, sticky="w")
rn = Entry(registry)
rn.grid(row=6, column=1, sticky="w")

item = Label(registry, text="Item Hired:")
item.grid(row=5, column=2, sticky="w")
ih = Entry(registry)
ih.grid(row=6, column=2, sticky="w")

quanti = Label(registry, text="Item Quantity:")
quanti.grid(row=7, column=1, sticky="w")
iq = Entry(registry)
iq.grid(row=8, column=1, sticky ="w")

#Submit Button
submit = Button(registry, text="Submit", command=validate).grid(row=9, column=2, sticky="e")

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

#Database
data = [
    
]

#Test Data
customertable.insert(parent="", index="end", iid=0, values=("Benedict", "Jed", "1", "Balloons", "43"))
customertable.insert(parent="", index="end", iid=1, values=("Large", "Harold", "2", "Lights", "1"))
customertable.insert(parent="", index="end", iid=2, values=("Sand", "Ivan", "3", "Dumbbells", "70"))

#Display Table
customertable.grid(column=0,row=0)

global count
count=3 # COUNT IS EQUAL TO 3 SINCE THERE ARE ALREADY 3 DUMMY DATA

for record in data:
    customertable.insert(parent="", index="end", iid=count, values=(record[0], record[1], record[2], record[3], record[4]))
    count += 1

#Append Data

def append():
    global count
    customertable.insert(parent="", index="end", iid=count, values=(ln.get(), fn.get(), rn.get(), ih.get(), iq.get()))
    count += 1

    fn.delete(0, END)
    ln.delete(0, END)
    rn.delete(0, END)
    ih.delete(0, END)
    iq.delete(0, END)


root.mainloop()