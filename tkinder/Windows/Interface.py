from tkinter import *
import tkinter.ttk as tk
from PIL import ImageTk, Image
import random
import MusicMath as mm
from MainScaffold import ProtectedBuffer

def create_page(window):
    
    #Create rows and collumn
    temp = tk.Label(window,text='')
    for i in range (1,6):
        for j in range (1,7):
            temp.grid(row=i,column=j)
    
    #Creates buttons      
    b1 = Button(window,text='Tuner',width=12,pady=10,bg='light green').grid(row=5,column=1,columnspan=2,padx=20,pady=20)
    b2 = Button(window,text='Train',width=12,pady=10,bg='light blue').grid(row=5,column=3,padx=20,pady=20,)
    b3 = Button(window,text='Stats',width=12,pady=10,bg='lavender').grid(row=5,column=5,columnspan=2,padx=20,pady=20)
    
    #Configures window to make middle row and column wider
    window.grid_rowconfigure(2, weight=2)
    window.grid_columnconfigure(3, weight=2)
    

def create_home_window(_buf: ProtectedBuffer = None):
    
    global root #Creates new window
    global buf #Create a shared buffer that persists between threads
    global tuner_clef
    if _buf is not None:
        buf = _buf

    #Allows for Bass Trebel and Alto images to appear
    def change_image(pos,IMG_Name='staff'):
        global tuner_clef
        tuner_clef=pos
        image_list = ['tkinder/Windows/images/bass_icon.png','tkinder/Windows/images/trebel_icon.png','tkinder/Windows/images/alto_icon.png']
        clef=''
        if(pos==0):
            clef='Bass'
        elif(pos==1):
            clef='Treble'
        else:
            clef='Alto'
        image_Note = 'tkinder/Windows/images/'+clef+'/'+IMG_Name+'.png'
        new_img=ImageTk.PhotoImage(Image.open(image_Note))
        image1.configure(image=new_img)
        image1.image=new_img
       
    root = Tk()
    root.title('Music Trainer')
    root.geometry('{}x{}'.format(800, 480)) #Width x Height
    tuner_clef=0
    #set Background
    bg = PhotoImage(file='tkinder/Windows/images/tamu_background.png')
    my_label = Label(root,image=bg).place(x=0, y=0, relwidth=1, relheight=1)

    #Creates page, buttons, textboxes and header
    create_page(root)                       #1st creates the grid and buttons    
    header = tk.Label(root,text='Tuner',font=("Arial",30,'bold')).grid(row=1,column=3,columnspan=2)
    
    #adds in temporary image and text
    my_file = 'tkinder/Windows/images/sample2.png'
    my_image = PhotoImage(file =my_file)
    image1 = Label(root,image=my_image)
    image1.grid(row=2,column=3)
    stringbuf = StringVar(root,value=('+/- ' + str(random.randint(0, 99)) + 'cents')) #text is stored in a StringVar object that the label can access by reference
    image_label = Label(root,textvariable=stringbuf,font=("Ludica Console",12,'bold'),width=9,anchor='e').grid(row=2,column=4) #label passively gets text from the textvariable
      
    #adds Bass Alto Trebel button functionality
    bass_button = Button(root,text='Bass',width=8,pady=5,bg='light green',font=("Arial",17,'bold'),command=lambda:[change_image(0)])
    bass_button.grid(row=4,column=1,columnspan=2,padx=20,pady=2)
    trebel_button = Button(root,text='Trebel',width=8,pady=5,bg='light blue',font=("Arial",17,'bold'),command=lambda:[change_image(1)])
    trebel_button.grid(row=4,column=3,padx=20,pady=2)
    alto_button = Button(root,text='Alto',width=8,pady=2,bg='lavender',font=("Arial",17,'bold'),command=lambda:[change_image(2)])
    alto_button.grid(row=4,column=5,columnspan=2,padx=20,pady=10)

    #Adds Trainer and Stats button functionality
    after_id = StringVar(root,"")
    train_button = Button(root,text='Train',width=12,pady=10, bg='light blue',command=lambda:[root.after_cancel(after_id.get()),root.destroy(),create_trainer_window()])
    train_button.grid(row=5,column=3,padx=20,pady=20)
    stats_button = Button(root,text='Stats',width=12,pady=10,bg='lavender',command=lambda:[root.after_cancel(after_id.get()),root.destroy(),create_stats_window()])
    stats_button.grid(row=5,column=5,columnspan=2,padx=20,pady=20)

    #Function for continuously updating deviation
    def display_deviation():
        value = buf.get()
        note = mm.closest_note(value)
        deviation = mm.cent_deviation(value,note)
        stringbuf.set(( "+" if deviation > 0 else "") + str(round(deviation,1)) + ' cents') #updates to the label's textvariable automatically display on the label
        
        #Automatic Note updating image
        global tuner_clef
        Temp_List=['B4','C4','F4','G4','D4']
        IMG_Name=random.choice(Temp_List)
        change_image(tuner_clef,IMG_Name)
        
        root.after(50, display_deviation) #recursively call this function in a new thread after 50 ms (non-blocking/responsive infinite loop)
    
    #Run window
    display_deviation() #start the ongoing background function
    root.mainloop()

def create_trainer_window():

    global trainer_window  #Creates new window
    
    #Allows for Bass Trebel and Alto images to appear
    def change_image(pos):
        image_list = ['tkinder/Windows/images/bass_icon.png','tkinder/Windows/images/trebel_icon.png','tkinder/Windows/images/alto_icon.png']
        new_img=ImageTk.PhotoImage(Image.open(image_list[pos]))
        image1.configure(image=new_img)
        image1.image=new_img
        
    trainer_window = Tk()
    trainer_window.title('Training')
    trainer_window.geometry('{}x{}'.format(800, 480)) #Width x Height
    
    #set Background
    bg = PhotoImage(file='tkinder/Windows/images/tamu_background2.png')
    my_label = Label(trainer_window,image=bg).place(x=0, y=0, relwidth=1, relheight=1)
    
    #Create trainer page with header, buttons and Textboxes
    create_page(trainer_window)                #Create Textboxes
    header = tk.Label(trainer_window,text='Training',font=("Arial",30,'bold')).grid(row=1,column=3,columnspan=2)
    
    #adds in temporary image and text actual note
    my_file = 'tkinder/Windows/images/train_icon.png'
    my_image = PhotoImage(file =my_file)
    image1 = Label(trainer_window,image=my_image)
    image1.grid(row=2,column=3)
    image_label = Label(trainer_window,text=('+/- ' + str(random.randint(0, 99)) + 'chz'),font=("Arial",12,'bold')).grid(row=2,column=4)

    target_file = "tkinder/Windows/images/sample2.png"
    target_image = PhotoImage(file=target_file)
    image2 = Label(trainer_window,image=target_image)
    image2.grid(row=2,column=2) 
    
    #adds Bass Alto Trebel button functionality
    bass_button = Button(trainer_window,text='Bass',width=8,pady=5,bg='light green',font=("Arial",17,'bold'),command=lambda:[change_image(0)])
    bass_button.grid(row=4,column=1,columnspan=2,padx=20,pady=2)
    trebel_button = Button(trainer_window,text='Trebel',width=8,pady=5,bg='light blue',font=("Arial",17,'bold'),command=lambda:[change_image(1)])
    trebel_button.grid(row=4,column=3,padx=20,pady=2)
    alto_button = Button(trainer_window,text='Alto',width=8,pady=2,bg='lavender',font=("Arial",17,'bold'),command=lambda:[change_image(2)])
    alto_button.grid(row=4,column=5,columnspan=2,padx=20,pady=10)
    
    #Add button Tuner and Stats functionality
    tuner_button = Button(trainer_window,text='Tuner',width=12,pady=10,bg='light green',command=lambda:[trainer_window.destroy(),create_home_window()])
    tuner_button.grid(row=5,column=1,columnspan=2,padx=20,pady=20)
    stats_button = Button(trainer_window,text='Stats',width=12,pady=10,bg='lavender',command=lambda:[trainer_window.destroy(),create_stats_window()])
    stats_button.grid(row=5,column=5,columnspan=2,padx=20,pady=20)
    
    #run window
    trainer_window.mainloop()
       
def create_stats_window():
    
    global stats_window  
    
    #Allows for Today Week and Month images to appear
    def change_image(pos):
        image_list = ["tkinder/Windows/images/TODAY.png","tkinder/Windows/images/WEEK.png","tkinder/Windows/images/MONTH.png"]
        new_img=ImageTk.PhotoImage(Image.open(image_list[pos]))
        image1.configure(image=new_img)
        image1.image=new_img
        
    #Create HomePage
    stats_window = Tk()
    stats_window.title('Your Statistics')
    stats_window.geometry('{}x{}'.format(800, 480)) #Width x Height
    
    #set Background
    bg = PhotoImage(file='tkinder/Windows/images/tamu_background3.png')
    my_label = Label(stats_window,image=bg).place(x=0, y=0, relwidth=1, relheight=1)
    
    #Creates page, buttons, and header
    create_page(stats_window)                               #1st creates the grid and button      
    header = tk.Label(stats_window,text='Your Progress',font=("Arial",25,'bold')).grid(row=1,column=3,columnspan=2)
    
    #add image
    my_file = 'tkinder/Windows/images/stat_icon.png'
    my_image = PhotoImage(file =my_file)
    image1 = Label(stats_window,image=my_image)
    image1.grid(row=2,column=3)
    image_label = Label(stats_window,text='Great!',font=("Arial",15,'bold')).grid(row=2,column=4)  
    
    #Create Progress Buttons
    b1 = Button(stats_window,text='TODAY',width=8,pady=2,bg='light green',font=("Arial",17,'bold'),command=lambda:[change_image(0)])
    b1.grid(row=4,column=1,columnspan=2,padx=20,pady=20)
    b2 = Button(stats_window,text='WEEK',width=8,pady=2,bg='light blue',font=("Arial",17,'bold'),command=lambda:[change_image(1)])
    b2.grid(row=4,column=3,padx=20,pady=20)
    b3 = Button(stats_window,text='MONTH',width=8,pady=2,bg='lavender',font=("Arial",17,'bold'),command=lambda:[change_image(2)])
    b3.grid(row=4,column=5,columnspan=2,padx=20,pady=20)
    
    #Add Tuner and Trainer Button functionality
    tuner_button = Button(stats_window,text='Tuner',width=12,pady=10, bg='light green',command=lambda:[stats_window.destroy(),create_home_window()])
    tuner_button.grid(row=5,column=1,columnspan=2,padx=20,pady=20)
    trainer_button = Button(stats_window,text='Train',width=12,pady=10, bg='light blue',command=lambda:[stats_window.destroy(),create_trainer_window()])
    trainer_button.grid(row=5,column=3,padx=20,pady=20)
    
    #Run window
    stats_window.mainloop()

if __name__=="__main__": #only run program immediately if called as a script
    create_home_window(ProtectedBuffer()) #Start program