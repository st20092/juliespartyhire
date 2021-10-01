from tkinter import *

root = Tk() #Creates a window
root.title ("Julie's Party Rental")
root.iconbitmap('D:\VSCODE\JuliesPartyHire\img\logo.ico')
root.geometry("912x513")
root.configure(bg="#F8F8F9")

#Title
title = Label(root, text="Julie's Party Hire").grid(row = 1, column = 1)

#Labels and Entry
firstname = Label(root, text="First Name:").grid(row = 2, column = 1, sticky = "w")
fn = Entry(root).grid(row = 3, column = 1)

lastname = Label(root, text="Last Name:").grid(row = 2, column = 2, sticky = "w")
ln = Entry(root).grid(row = 3, column = 2)

recepnum = Label(root, text="Recipient Number:").grid(row = 4, column = 1, sticky = "w")
rn = Entry(root).grid(row = 5, column = 1)

item = Label(root, text="Item Hired:") .grid(row = 4, column = 2, sticky = "w")
ih = Entry(root).grid(row = 5, column = 2)

quanti = Label(root, text="Item Quantity:") .grid(row = 6, column = 1, sticky = "w")
iq = Entry(root).grid(row = 7, column = 1)

#Submit Button
submit = Button(root, text="Submit").grid(row = 8, column = 2, sticky = "e")

root.mainloop()