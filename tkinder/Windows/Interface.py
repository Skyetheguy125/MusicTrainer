from tkinter import *
import tkinter.ttk as tk
from PIL import ImageTk, Image

def create_page(window):
    #Create rows and collumn
    temp = tk.Label(window,text='')
    for i in range (1,6):
        for j in range (1,7):
            temp.grid(row=i,column=j)
    
    #Creates buttons      
    b1 = Button(window,text='Tuner',width=12,pady=10,bg='light green').grid(row=5,column=1,columnspan=2,padx=20,pady=20)
    b2 = Button(window,text='Train',width=12,pady=10,bg='light blue').grid(row=5,column=3,padx=20,pady=20)
    b3 = Button(window,text='Stats',width=12,pady=10,bg='lavender').grid(row=5,column=5,columnspan=2,padx=20,pady=20)
    
    #Configures window to make middle row and column wider
    window.grid_rowconfigure(2, weight=2)
    window.grid_columnconfigure(3, weight=2)
     
def create_textboxes(window):
        #Create Textbox
    t1_label = Label(window,text='Bass:',width=11,bg='light green').grid(row=3,column=1,pady=3,columnspan=2)
    t1 = Text(window,height=1,width=10).grid(row=4,column=1,columnspan=2)
    t2_label = Label(window,text='Trebel:',width=11,bg='light blue').grid(row=3,pady=3,column=3)
    t2 = Text(window,height=1,width=10).grid(row=4,column=3)
    t3_label = Label(window,text='Alto:',width=11,bg='lavender').grid(row=3,column=5,pady=3,columnspan=2)
    t3 = Text(window,height=1,width=10).grid(row=4,column=5,columnspan=2)

def create_home_window():
    #destroys other windows if open
    try:
        trainer_window.destroy()
    except TclError:
        try:
            stats_window.destroy()
        except TclError as x:
            pass
    except NameError:
        pass

    global root #Creates new window
    root = Tk()
    root.title('Music Trainer')
    root.geometry('{}x{}'.format(800, 480)) #Width x Height
    
    #set Background
    bg = PhotoImage(file='images/tamu_background.png')
    my_label = Label(root,image=bg)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)

    #Creates page, buttons, textboxes and header
    create_page(root)                       #1st creates the grid and buttons
    create_textboxes(root)                  #2nd Create Textboxes      
    header = tk.Label(root,text='Tuner',font=("Arial",30,'bold'))
    header.grid(row=1,column=3,columnspan=2)
    
    #adds in temporary image and text
    my_file = 'images/sample2.png'
    my_image = PhotoImage(file =my_file)
    image1 = Label(root,image=my_image)
    image1.grid(row=2,column=3)
    image_label = Label(root,text='+/- 15chz',font=("Arial",12,'bold'))
    image_label.grid(row=2,column=4)
            
    #Adds Trainer and Stats button functionality
    train_button = Button(root,text='Train',width=12,pady=10, bg='light blue',command=create_trainer_window)
    train_button.grid(row=5,column=3,padx=20,pady=20)
    stats_button = Button(root,text='Stats',width=12,pady=10,bg='lavender',command=create_stats_window)
    stats_button.grid(row=5,column=5,columnspan=2,padx=20,pady=20)
    
    #Run window
    root.mainloop()

def create_trainer_window():
    #destroys other winsows if open
    try:
        root.destroy()
    except TclError as e:
        stats_window.destroy()
    
    global trainer_window  #Creates new window
    trainer_window = Tk()
    trainer_window.title('Training')
    trainer_window.geometry('{}x{}'.format(800, 480)) #Width x Height
    
    #set Background
    bg = PhotoImage(file='images/tamu_background.png')
    my_label = Label(trainer_window,image=bg)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    #Create trainer page with header, buttons and Textboxes
    create_page(trainer_window)
    create_textboxes(trainer_window)                  #Create Textboxes
    header = tk.Label(trainer_window,text='Training',font=("Arial",30,'bold'))
    header.grid(row=1,column=3,columnspan=2)
    
    #adds in temporary image and text
    my_file = 'images/train_icon.png'
    my_image = PhotoImage(file =my_file)
    image1 = Label(trainer_window,image=my_image)
    image1.grid(row=2,column=3)
    image_label = Label(trainer_window,text='+/- 15chz',font=("Arial",12,'bold'))
    image_label.grid(row=2,column=4) 
    
    #Add button Tuner and Stats functionality
    tuner_button = Button(trainer_window,text='Tuner',width=12,pady=10,bg='light green',command=create_home_window)
    tuner_button.grid(row=5,column=1,columnspan=2,padx=20,pady=20)
    stats_button = Button(trainer_window,text='Stats',width=12,pady=10,bg='lavender',command=create_stats_window)
    stats_button.grid(row=5,column=5,columnspan=2,padx=20,pady=20)
    
    #run window
    trainer_window.mainloop()
       
def create_stats_window():
    #destroys other windows if open
    try:
        root.destroy()
    except TclError as e:
        trainer_window.destroy()
        
    global stats_window
    
    #Create HomePage
    stats_window = Tk()
    stats_window.title('Your Statistics')
    stats_window.geometry('{}x{}'.format(800, 480)) #Width x Height
    
    #set Background
    bg = PhotoImage(file='images/tamu_background.png')
    my_label = Label(stats_window,image=bg)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    #Creates page, buttons, and header
    create_page(stats_window)                               #1st creates the grid and button      
    header = tk.Label(stats_window,text='Your Progress',font=("Arial",25,'bold'))  #Header
    header.grid(row=1,column=3,columnspan=2)
    
    #add image
    my_file = 'images/stat_icon.png'
    my_image = PhotoImage(file =my_file)
    image1 = Label(stats_window,image=my_image)
    image1.grid(row=2,column=3)
    image_label = Label(stats_window,text='Great!',font=("Arial",15,'bold'))
    image_label.grid(row=2,column=4)  
    
    #Create Progress Buttons
    b1 = Button(stats_window,text='TODAY',width=12,pady=10,bg='light green',font='bold')
    b1.grid(row=4,column=1,columnspan=2,padx=20,pady=20)
    b2 = Button(stats_window,text='WEEK',width=12,pady=10,bg='light blue',font='bold')
    b2.grid(row=4,column=3,padx=20,pady=20)
    b3 = Button(stats_window,text='MONTH',width=12,pady=10,bg='lavender',font='bold')
    b3.grid(row=4,column=5,columnspan=2,padx=20,pady=20)
    
    #Add Tuner and Trainer Button functionality
    tuner_button = Button(stats_window,text='Tuner',width=12,pady=10, bg='light green',command=create_home_window)
    tuner_button.grid(row=5,column=1,columnspan=2,padx=20,pady=20)
    trainer_button = Button(stats_window,text='Train',width=12,pady=10, bg='light blue',command=create_trainer_window)
    trainer_button.grid(row=5,column=3,padx=20,pady=20)
    
    #Run window
    stats_window.mainloop()

create_home_window() #Start program