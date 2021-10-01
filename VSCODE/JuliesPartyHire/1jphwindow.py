from tkinter import *

root = Tk() #Creates a window
root.title ("Julie's Party Rental")
root.iconbitmap('D:\VSCODE\JuliesPartyHire\img\logo.ico')
root.geometry("912x513")
root.configure(bg="#F8F8F9")

title = Label(root, text="Julie''s Party Hire").grid(row = 1, column = 1)


root.mainloop()
