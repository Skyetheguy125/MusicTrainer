# import tkinter module
from tkinter import *
from tkinter.ttk import *

# creating main tkinter window/toplevel
master = Tk()
master.geometry('320x150')
master.title('Front Demo')
# topFrame = Frame(master)
# topFrame.pack()
# bottomFrame = Frame(master)
# bottomFrame.pack(side=BOTTOM)
# this will create a label widget
l1 = Label(master, text = "")
l2 = Label(master, text = "")

# # grid method to arrange labels in respective
# # rows and columns as specified
l1.grid(row = 1, column = 0, sticky = W, pady = 2)
l2.grid(row = 2, column = 0, sticky = W, pady = 2)

# # entry widgets, used to take entry from user
# e1 = Entry(master)
# e2 = Entry(master)

# # this will arrange entry widgets
# e1.grid(row = 0, column = 1, pady = 2)
# e2.grid(row = 1, column = 1, pady = 2)

# checkbutton widget
# c1 = Checkbutton(master, text = "Preserve")
# c1.grid(row = 2, column = 0, sticky = W, columnspan = 2)

# adding image (remember image should be PNG and not JPG)
img = PhotoImage(file = r"./tkinder/Testing_Files/Staff.png")
img1 = img.subsample(2, 2)

# setting image with the help of label
Label(master, image = img1).grid(row = 0, column = 2,
	columnspan = 3, rowspan = 2, padx = 5, pady = 5)

# button widget
b1 = Button(master, text = "Tuner")
b2 = Button(master, text = "Trainer")
b3 = Button(master, text = "Statistics")

# arranging button widgets
b1.grid(row = 5, column = 2, sticky = E)
b2.grid(row = 5, column = 3, sticky = E)
b3.grid(row = 5, column = 4, sticky = E)

# infinite loop which can be terminated
# by keyboard or mouse interrupt
mainloop()
