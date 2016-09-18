from Tkinter import *
import ttk

root = Tk()

content = ttk.Frame(root, padding=(3,3,8,12))
frame = Text(content, borderwidth=5, relief="sunken", width=120, height=80)
namelbl = ttk.Label(content, text="Glossary")
namelbl.config(font=("Courier", 20))


#name = ttk.Entry(content)

onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()

onevar.set(True)
twovar.set(False)
threevar.set(True)

one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Save")
cancel = ttk.Button(content, text="Scan")

content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=(N, S, E, W))
#namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
namelbl.grid(column=2, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
#one.grid(column=4, row=3)
#two.grid(column=1, row=3)
#three.grid(column=3, row=3)
ok.grid(column=0, row=3)
cancel.grid(column=1, row=3)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=2)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

root.mainloop()