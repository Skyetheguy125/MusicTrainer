from tkinter import *

root =  Tk()
root.title("Config test")
root.geometry('400x400')


global my_label
my_label  = Label(root,text="things",bg="grey")
my_label.pack(pady=10)

def something():
    my_label.config(text="This is new text")
    myButton.config(text="configged")


myButton = Button(root,text="click me",command=something, fg="blue")
myButton.pack()

root.mainloop()