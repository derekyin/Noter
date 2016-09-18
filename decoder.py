import analyze
import tkinter

def decode (lst):
    #text = text from textfield
    newText = ""
    #bold keywords
    for key in lst:
        for word in key["position"]:
            newText += text[:word["position"] + 1]
            text = text[:word["position"]]  #truncate original text
            newText += "<b>" + text[:key["word"]] + "</b>" #bold keyword
            text = text[:text[:key["word"] + 1] #truncate original text
        newText += text #add remaining text
        text = newText #reset text for next wave of bolding
                
    return newText
        
