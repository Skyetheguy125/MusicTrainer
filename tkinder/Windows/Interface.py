from tkinter import *
import tkinter.ttk as tk

def create_home_window():
    try:
        trainer_window.destroy() #destroys other windows if open
    except TclError:
        try:
            stats_window.destroy()
        except TclError as x:
            pass

    global root
    
    #Create HomePage
    root = Tk()
    root.title('Music Trainer')
    root.geometry('{}x{}'.format(800, 480)) #Width x Height
    
    #Creating grid rows
    r1 = tk.Label(root,text='')
    r1.grid(row=1,column=1)
    r2 = tk.Label(root,text='')
    r2.grid(row=2,column=1)
    r3 = tk.Label(root,text='')
    r3.grid(row=3,column=1)
    r5 = tk.Label(root,text='')
    r5.grid(row=5,column=1)
    
    #Create grid Columns
    c1 = tk.Label(root,text='')
    c1.grid(row=1,column=2)
    c2 = tk.Label(root,text='')
    c2.grid(row=1,column=2)
    c3 = tk.Label(root,text='Tuner')
    c3.grid(row=1,column=3,columnspan=2)
    c4 = tk.Label(root,text='')
    c4.grid(row=1,column=4)
    c5 = tk.Label(root,text='')
    c5.grid(row=1,column=5)
    c6 = tk.Label(root,text='')
    c6.grid(row=1,column=6)
    
    #Create Buttons
    b1 = Button(root,text='Tuner',width=12,pady=10)
    b1.grid(row=5,column=1,columnspan=2,padx=20,pady=20)
    b2 = Button(root,text='Train',width=12,pady=10, command=create_trainer_window)
    b2.grid(row=5,column=3,padx=20,pady=20)
    b3 = Button(root,text='Stats',width=12,pady=10,command=create_stats_window)
    b3.grid(row=5,column=5,columnspan=2,padx=20,pady=20)
    
    #Create Textbox
    t1_label = Label(root,text='Bass:')
    t1_label.grid(row=3,column=1,columnspan=2)
    t1 = Text(root,height=1,width=10)
    t1.grid(row=4,column=1,columnspan=2)
    t2_label = Label(root,text='Trebel:')
    t2_label.grid(row=3,column=3)
    t2 = Text(root,height=1,width=10)
    t2.grid(row=4,column=3)
    t3_label = Label(root,text='Alto:')
    t3_label.grid(row=3,column=5,columnspan=2)
    t3 = Text(root,height=1,width=10)
    t3.grid(row=4,column=5,columnspan=2)
    
    #add image
    my_image = PhotoImage(file ='images/sample2.png')
    image1 = Label(root,image=my_image)
    image1.grid(row=2,column=3)
    image_label = Label(root,text='+/- 15chz')
    image_label.grid(row=2,column=4)
    root.grid_rowconfigure(2, weight=2)
    root.grid_columnconfigure(3, weight=2)
    
    root.mainloop()


def create_trainer_window():
    
    try:
        root.destroy() #destroys other winsows if open
    except TclError as e:
        stats_window.destroy()
    
    global trainer_window
    
    trainer_window = Tk()
    trainer_window.title('Training')
    trainer_window.geometry('{}x{}'.format(800, 480)) #Width x Height
    
        #Creating grid rows
    r1 = tk.Label(trainer_window,text='')
    r1.grid(row=1,column=1)
    r2 = tk.Label(trainer_window,text='')
    r2.grid(row=2,column=1)
    r3 = tk.Label(trainer_window,text='')
    r3.grid(row=3,column=1)
    r5 = tk.Label(trainer_window,text='')
    r5.grid(row=5,column=1)
    
    #Create grid Columns
    c1 = tk.Label(trainer_window,text='')
    c1.grid(row=1,column=2)
    c2 = tk.Label(trainer_window,text='')
    c2.grid(row=1,column=2)
    c3 = tk.Label(trainer_window,text='Training')
    c3.grid(row=1,column=3,columnspan=2)
    c4 = tk.Label(trainer_window,text='')
    c4.grid(row=1,column=4)
    c5 = tk.Label(trainer_window,text='')
    c5.grid(row=1,column=5)
    c6 = tk.Label(trainer_window,text='')
    c6.grid(row=1,column=6)
    
    #Create 3 Buttons
    b1 = Button(trainer_window,text='Tuner',width=12,pady=10,command=create_home_window)
    b1.grid(row=5,column=1,columnspan=2,padx=20,pady=20)
    b2 = Button(trainer_window,text='Train',width=12,pady=10)
    b2.grid(row=5,column=3,padx=20,pady=20)
    b3 = Button(trainer_window,text='Stats',width=12,pady=10,command=create_stats_window)
    b3.grid(row=5,column=5,columnspan=2,padx=20,pady=20)
    
    #Create 3 Textbox
    t1_label = Label(trainer_window,text='Bass:')
    t1_label.grid(row=3,column=1,columnspan=2)
    t1 = Text(trainer_window,height=1,width=10)
    t1.grid(row=4,column=1,columnspan=2)
    t2_label = Label(trainer_window,text='Trebel:')
    t2_label.grid(row=3,column=3)
    t2 = Text(trainer_window,height=1,width=10)
    t2.grid(row=4,column=3)
    t3_label = Label(trainer_window,text='Alto:')
    t3_label.grid(row=3,column=5,columnspan=2)
    t3 = Text(trainer_window,height=1,width=10)
    t3.grid(row=4,column=5,columnspan=2)
    
    #adds in temporary image and text
    image2 = PhotoImage(file ='images/train_icon.png')
    image1 = Label(trainer_window,image=image2)
    image1.grid(row=2,column=3)
    image_label = Label( trainer_window,text='+/- 15chz')
    image_label.grid(row=2,column=4)
    
    #configures window
    trainer_window.grid_rowconfigure(2, weight=2)
    trainer_window.grid_columnconfigure(3, weight=2)
    
    #run the window
    trainer_window.mainloop()
    

def create_stats_window():
    
    try:
        root.destroy() #destroys other windows if open
    except TclError as e:
        trainer_window.destroy()
        
    global stats_window
    
    #Create HomePage
    stats_window = Tk()
    stats_window.title('Your Statistics')
    stats_window.geometry('{}x{}'.format(800, 480)) #Width x Height
    
    #Creating grid rows
    r1 = tk.Label(stats_window,text='')
    r1.grid(row=1,column=1)
    r2 = tk.Label(stats_window,text='')
    r2.grid(row=2,column=1)
    r3 = tk.Label(stats_window,text='')
    r3.grid(row=3,column=1)
    r5 = tk.Label(stats_window,text='')
    r5.grid(row=5,column=1)
    
    #Create grid Columns
    c1 = tk.Label(stats_window,text='')
    c1.grid(row=1,column=2)
    c2 = tk.Label(stats_window,text='')
    c2.grid(row=1,column=2)
    c3 = tk.Label(stats_window,text='Your Stats')
    c3.grid(row=1,column=3,columnspan=2)
    c4 = tk.Label(stats_window,text='')
    c4.grid(row=1,column=4)
    c5 = tk.Label(stats_window,text='')
    c5.grid(row=1,column=5)
    c6 = tk.Label(stats_window,text='')
    c6.grid(row=1,column=6)
    
    #Create Progress Buttons
    b1 = Button(stats_window,text='TODAY',width=12,pady=10)
    b1.grid(row=4,column=1,columnspan=2,padx=20,pady=20)
    b2 = Button(stats_window,text='WEEK',width=12,pady=10)
    b2.grid(row=4,column=3,padx=20,pady=20)
    b3 = Button(stats_window,text='MONTH',width=12,pady=10)
    b3.grid(row=4,column=5,columnspan=2,padx=20,pady=20)
    
    #Create Buttons
    b4 = Button(stats_window,text='Tuner',width=12,pady=10, command=create_home_window)
    b4.grid(row=5,column=1,columnspan=2,padx=20,pady=20)
    b5 = Button(stats_window,text='Train',width=12,pady=10, command=create_trainer_window)
    b5.grid(row=5,column=3,padx=20,pady=20)
    b6 = Button(stats_window,text='Stats',width=12,pady=10)
    b6.grid(row=5,column=5,columnspan=2,padx=20,pady=20)
    
    #add image
    my_image = PhotoImage(file ='images/stat_icon.png')
    image1 = Label(stats_window,image=my_image)
    image1.grid(row=2,column=3)
    image_label = Label(stats_window,text='Good Progress')
    image_label.grid(row=2,column=4)
    stats_window.grid_rowconfigure(2, weight=2)
    stats_window.grid_columnconfigure(3, weight=2)
    
    stats_window.mainloop()
  


create_home_window()
