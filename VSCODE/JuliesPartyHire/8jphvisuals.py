from tkinter import *
from tkinter import ttk
from tkinter import font
from typing import Collection

root = Tk() #Creates a window
root.title ("Julie's Party Hire")
root.iconbitmap('D:\VSCODE\JuliesPartyHire\img\logo.ico')
root.geometry("912x513")
root.configure(bg="#F8F8F9")

#Visuals
style = ttk.Style()
#Theme Color
style.theme_use("clam")

#Table Visuals
style.configure("Treeview",
    background="#F8F8F9",
    foreground="#474747",
    rowheight=40,
    fieldbackground="#f8f8f9",
    font=("Corbel Light",13),
    
)

style.configure("Treeview.Heading",
    font=("Corbel Light",12),
)


#Registry Visuals

#Database Visuals

#Tab Visuals
style.configure("TNotebook.Tab",
    font=("Corbel Light",12),
    width=55,
)

#Validation

def validate ():
    incorrectinput = 0

    #First Name Correct
    if len(fn.get()) > 0 and len(fn.get()) <= 200:
        firstname.config(text="First Name:", fg="#474747")

    #First Name Incorrect
    if len(fn.get()) == 0:
        firstname.config(text="First Name: Missing", fg="red")
        incorrectinput = 1
    if len(fn.get()) > 200:
        firstname.config(text="First Name: 200 Character Limit", fg="red")
        incorrectinput = 1


    #Last Name Correct
    if len(ln.get()) > 0 and len(ln.get()) <= 200:
        lastname.config(text = "Last Name:", fg="#474747")

    #Last Name Incorrect
    if len(ln.get()) == 0 or len(ln.get()) > 200:
        lastname.config(text = "Last Name: Missing", fg="red")
        incorrectinput = 1
    if len(ln.get()) > 200:
        lastname.config(text = "Last Name: 200 Character Limit", fg="red")
        incorrectinput = 1
    

    #Recipient Number
    if (rn.get().isdigit()):
        #Recipient Number Correct
        if int(rn.get()) >= 0:
            recipnum.config(text="Recipient Number:", fg="#474747")
        #Recipient Number Incorrect
        if int(rn.get()) <= 0:
            recipnum.config(text="Recipient Number: Missing", fg="red")
            incorrectinput = 1
        
    else:
        recipnum.config(text="Recipient Number: Missing", fg="red")
        incorrectinput = 1

    #Item Hired Correct
    if len(ih.get()) > 0 and len(ih.get()) <= 50:
        item.config(text="Item Hired:", fg="#474747")

    #Item Hired Incorrect
    if len(ih.get()) == 0 :
        item.config(text="Item Hired: Missing", fg="red")
        incorrectinput = 1
    if len(ih.get()) > 50 :
        item.config(text = "Item Hired: 50 Character Limit", fg="red")
        incorrectinput = 1
    

    #Item Quantity
    if (iq.get().isdigit()):
        #Item Quantity Correct
        if int(iq.get()) > 0 or int(iq.get()) <= 500:
            quanti.config(text="Item Quantity:", fg="#474747")
        #Item Quantity Incorrect
        if int(iq.get()) <= 0 or int(iq.get()) > 500:
            quanti.config(text="Item Quantity: 1 - 500", fg="red")
            incorrectinput = 1
        
    else:
        quanti.config(text="Item Quantity: Missing", fg="red")
        incorrectinput = 1

    if incorrectinput == 0 :
        append()

#Title
title = Label(root, text="Julie's Party Hire", fg="#474747", bg="#F8F8F9", padx=15, pady=10)
title.grid(row = 1, column = 1, sticky= "w")
title.config(font=("Corbel Light",40))


#Tabs
tabs = ttk.Notebook(root)
tabs.grid(row = 2, column=1, pady=10)

registry = Frame(tabs, width = 912, height = 413, borderwidth=0, highlightthickness=0)
registry.config(background="#F8F8F9", pady=25)
database = Frame(tabs, width = 912, height = 413, borderwidth=0, highlightthickness=0)

registry.pack(fill="both", expand="1")
database.pack(fill="both", expand="1")

tabs.add(registry, text="Registry")
tabs.add(database, text="Database")

## REGISTRY TAB ##
#Labels and Entry
firstname = Label(registry, text = "First Name:", pady=15, padx=93, fg="#474747", bg="#F8F8F9")
firstname.grid(row = 3, column = 1, sticky = "w")
firstname.config(font=("Bahnschrift Light",15))
fn = Entry(registry, width=22)
fn.grid(row=4, column=1, sticky="w", padx=90)
fn.config(font=("Corbel Light",18))

lastname = Label(registry, text="Last Name:", pady=15, padx=65, fg="#474747", bg="#F8F8F9")
lastname.grid(row=3, column=2, sticky="w")
lastname.config(font=("Bahnschrift Light",15))
ln = Entry(registry, width=22)
ln.grid(row=4, column=2, stick ="w", padx=60)
ln.config(font=("Corbel Light",18))

recipnum = Label(registry, text="Recipient Number:", pady=15, padx=93, fg="#474747", bg="#F8F8F9")
recipnum.grid(row=5, column=1, sticky="w")
recipnum.config(font=("Bahnschrift Light",15))
rn = Entry(registry, width=22)
rn.grid(row=6, column=1, sticky="w", padx=90)
rn.config(font=("Corbel Light",18))

item = Label(registry, text="Item Hired:", pady=15, padx=65, fg="#474747", bg="#F8F8F9")
item.grid(row=5, column=2, sticky="w")
item.config(font=("Bahnschrift Light",15))
ih = Entry(registry, width=22)
ih.grid(row=6, column=2, sticky="w", padx=60)
ih.config(font=("Corbel Light",18))

quanti = Label(registry, text="Item Quantity:", pady=15, padx=93, fg="#474747", bg="#F8F8F9")
quanti.grid(row=7, column=1, sticky="w")
quanti.config(font=("Bahnschrift Light",15))
iq = Entry(registry, width=22)
iq.grid(row=8, column=1, sticky ="w", padx=90)
iq.config(font=("Corbel Light",18))

#Submit Button
submit = Button(registry, text="Submit", command=validate, bg="#F8F8F9")
submit.grid(row=9, column=2, sticky="e")
submit.config(font=("Bahnschrift Light",13))

## DATABASE TAB ##
#Tree View Frame
tableframe = Frame(database, borderwidth=0, highlightthickness=0)
tableframe.grid(row=0,column=0)
#Tree View
customertable = ttk.Treeview(tableframe, height=7)
#Tree View Scroll
tablescroll = Scrollbar(tableframe, orient=VERTICAL)
tablescroll.pack(side=RIGHT, fill=Y)
tablescroll.config(command=customertable.yview)

#Columns
customertable['columns'] = ("Last Name", "First Name", "Recipient Number", "Item Hired", "Quantity")
customertable.column("#0", width=0, stretch=NO)
customertable.column("Last Name", anchor=CENTER, width=178, stretch=NO)
customertable.column("First Name", anchor=CENTER, width=178, stretch=NO)
customertable.column("Recipient Number", anchor=CENTER, width=178, stretch=NO)
customertable.column("Item Hired", anchor=CENTER, width=178, stretch=NO)
customertable.column("Quantity", anchor=CENTER, width=178, stretch=NO)

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
customertable.insert(parent="", index="end", iid=0, values=("Benedict", "Jed", "0", "Balloons", "43"))
customertable.insert(parent="", index="end", iid=1, values=("Large", "Harold", "1", "Lights", "1"))
customertable.insert(parent="", index="end", iid=2, values=("Sand", "Ivan", "2", "Dumbbells", "70"))

#Display Table
customertable.pack(side=LEFT)

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

#Removing Data

def removeselected():
    global record
    selected = customertable.selection()
    for record in selected:
        customertable.delete(record)

def removeall():
    global record
    for record in customertable.get_children():
        customertable.delete(record)

#Remove Frame
removesection = LabelFrame(database, borderwidth=0, highlightthickness=0)
removesection.grid(row=1, column=0, padx=10)
removesection.configure(pady=17)

#Removing Buttons
deleteall = Button(removesection, text="Remove All Data", command=removeall)
deleteall.grid(row=0, column=0)
deleteall.config(font=("Bahnschrift Light", 12))

deleteselected = Button(removesection, text="Remove Selected Data", command=removeselected)
deleteselected.grid(row=0, column=1, padx=50)
deleteselected.config(font=("Bahnschrift Light", 12))




root.mainloop()