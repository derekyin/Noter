from Tkinter import *
import tkMessageBox

def helloCallBack():
   tkMessageBox.showinfo( "Submitted", "Processing")

root = Tk()
T = Text(root, height=25, width=100)
T.pack()
quote = """Sample text"""
T.insert(END, quote)

W = Button(root, text ="Scan", command = helloCallBack)
W.pack()
W = Button(root, text ="Save", command = helloCallBack)
W.pack()


mainloop()


