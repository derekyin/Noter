import webbrowser
from Tkinter import *
import ttk
import analyze
import re
root = Tk()

content = ttk.Frame(root, padding=(3,3,8,12))
display = True
frame = Text(content, borderwidth=5, relief="sunken", width=120, height=80)
namelbl = ttk.Label(content, text="Glossary")
namelbl.config(font=("Courier", 20))
link = []
root.geometry('{}x{}'.format(1200,600))
root.minsize(width = 1200, height = 600)
root.title("noter")

def retrieve_input():
    input = frame.get("1.0",END)
    return input
def callback(string):
        webbrowser.open_new(r"http://www.google.com/search?q=%s" % string)

def decode (lst):
    text = retrieve_input()
    newText = ""
    #bold keywords
    for key in lst:
        #newText = ""
        for word in key["position"]:
            word = int(word)
            newText += text[:word]
            text = text[word:]  #truncate original text
            newText += "<<  " + text[:len(key["word"])] + "  >>" #bold keyword
            text = text[len(key["word"]):] #truncate original text
        newText += text #add remaining text
        text = "" #reset text for next wave of bolding
        
    i = 0
    for key in lst:
        link.append( Label(root, text=key["word"], fg="blue", cursor="hand2"))
        link[i].bind("<Button-1>", lambda x: callback(key["word"]))
        link[i].pack(fill = X)
        link[i].place (x=1050, y = 50 * (i + 1))
        i += 1
    return newText

def write_text():
    text_file = open("Output.txt", "w")
    lst = analyze.processText (retrieve_input())
    text_file.write("Glossary\n")
    for key in lst:
        text_file.write("%s" %key["word"])

def debugPrint():
    print "Yes"

#name = ttk.Entry(content)

save = ttk.Button(content, text="Save", command = debugPrint)

print "Got here"
scan = ttk.Button(content, text="Scan", command= lambda:frame.insert(END,"\n" + decode(analyze.processText(retrieve_input()))))

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

mainloop()


