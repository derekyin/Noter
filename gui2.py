from Tkinter import *
import ttk
import analyze

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
save = ttk.Button(content, text="Save", command = write_text())
scan = ttk.Button(content, text="Scan", command= decode(analyze.processword(retrieve_input())))

content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=(N, S, E, W))
#namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
namelbl.grid(column=2, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
#one.grid(column=4, row=3)
#two.grid(column=1, row=3)
#three.grid(column=3, row=3)
save.grid(column=0, row=3)
scan.grid(column=1, row=3)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=2)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

root.mainloop()

def decode (lst):
    #text = text from textfield
    newText = ""
    #bold keywords
    for key in lst:
        for word in key["position"]:
            newText += text[:word["position"] + 1]
            text = text[:word["position"]]  #truncate original text
            newText += "<b>" + text[:key["word"]] + "</b>" #bold keyword
            text = text[:text[:key["word"] + 1]] #truncate original text
        newText += text #add remaining text
        text = newText #reset text for next wave of bolding
                
    return newText

def retrieve_input():
    input = self.myText_Box.get("1.0",END)

def write_text():
    text_file = open("Output.txt", "w")