from tkinter import *

root =  Tk()

def myClick():
    myLabel = Label(root,text="button clicked")
    myLabel.pack()

myButton = Button(root,text="click me",command=myClick, fg="blue")
myButton.pack()

root.mainloop()