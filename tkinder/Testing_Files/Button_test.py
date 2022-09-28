from tkinter import *

root =  Tk()

def myClick():
    myLabel = Label(root,text="button clicked")
    myLabel.pack()

myButton = Button(root,text="click me",command=myClick, fg="blue",bg="#000000")
myButton.pack()

root.mainloop()