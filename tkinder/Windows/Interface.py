from tkinter import *
import tkinter.ttk as tk
from PIL import ImageTk, Image
import random
import MusicMath as mm
from MainScaffold import ProtectedBuffer

def change_image(image_name,image=None):
    try:
        t_image = Image.open(image_name)
        im_resized = t_image.crop((0,30,t_image.width,t_image.height-50))
        (width, height) = (int(float(im_resized.width) // 1.5), int(float(im_resized.height) // 1.5))
        im_resized = im_resized.resize((width, height))
        new_img=ImageTk.PhotoImage(im_resized)
    except FileNotFoundError as e:
        image_name = 'tkinder/Windows/images/'+tuner_clef+'/staff.png'
        print("FileNotFoundError [{errno}]: {errstr} \"{filename}\"".format(errno=e.errno,errstr=e.strerror,filename=e.filename))
        t_image = Image.open(image_name)
        im_resized = t_image.crop((0,30,t_image.width,t_image.height-50))

        (width, height) = (int(float(im_resized.width) // 1.5), int(float(im_resized.height) // 1.5))
        im_resized = im_resized.resize((width, height))
        new_img=ImageTk.PhotoImage(im_resized)
    
    image.configure(image=new_img)

    image.image=new_img

#Allows clef-changing as an independent operation inside a lambda expression
def change_clef(clef):
    '''
    clef - 'Bass', 'Treble', or 'Alto'. Raises exception on other input.
    modifies global variable tuner_clef to be equal to clef.
    '''
    global tuner_clef
    if clef not in {'Bass','Treble','Alto'}:
        raise Exception("Clef {_clef} does not exist".format(_clef=clef))
    tuner_clef = clef

def create_page(window):
    
    #Create rows and collumn
    temp = tk.Label(window,text='')
    for i in range (1,6):
        for j in range (1,7):
            temp.grid(row=i,column=j)
    
    #Creates buttons      
    b1 = Button(window,text='Tuner',width=12,pady=10,bg='light green', bd=5, relief ='raised', overrelief='sunken').grid(row=5,column=1,columnspan=2,padx=20,pady=20)
    b2 = Button(window,text='Train',width=12,pady=10,bg='light blue', bd=5, relief ='raised', overrelief='sunken').grid(row=5,column=3,padx=20,pady=20,)
    b3 = Button(window,text='Stats',width=12,pady=10,bg='lavender', bd=5, relief ='raised', overrelief='sunken').grid(row=5,column=5,columnspan=2,padx=20,pady=20)
    
    #Configures window to make middle row and column wider
    window.grid_rowconfigure(2, weight=2)
    window.grid_columnconfigure(3, weight=2)   

def create_welcome_window(_signal_buf: ProtectedBuffer = None, _target_buf: ProtectedBuffer = None):
    global welcome_window
    global signal_buf
    global target_buf
    if _signal_buf is not None:
        signal_buf = _signal_buf
    if _target_buf is not None:
        target_buf = _target_buf
        
    #Creating default window. Sizing, background and buttons
    welcome_window = Tk()
    welcome_window.title('CSCE 483 Music Trainer')
    welcome_window.geometry('{}x{}'.format(800, 480)) #Width x Height
    bg = PhotoImage(file='tkinder/Windows/images/tamu_background0.png')
    my_label = Label(welcome_window,image=bg).place(x=0, y=0, relwidth=1, relheight=1)
    
        #Create rows and collumn
    temp = tk.Label(welcome_window,text='')
    for i in range (1,10):
        for j in range (1,7):
            temp.grid(row=i,column=j)
    
    header = tk.Label(welcome_window,text='Welcome to Music Trainer v1.0',font=("Arial",32,'bold')).grid(row=1,column=3,columnspan=4,pady=10)
    
    #start and close button added to default window
    start_button = Button(welcome_window,text='Start',width=10,padx=1,pady=5,bg='light green',font=("Arial",12,'bold'),bd=5, relief ='raised', overrelief='sunken',command=create_home_window).grid(row=2,column=3,rowspan=2,pady=20)
    close_button = Button(welcome_window,text='Leave',width=10,padx=1,pady=5,bg='red',font=("Arial",12,'bold'),relief ='raised', overrelief='sunken',command=welcome_window.destroy).grid(row=3,column=3,rowspan=2,pady=20)
    welcome_window.grid_rowconfigure(2, weight=2)
    welcome_window.grid_columnconfigure(3, weight=2)   
        
    #lets window become full screen (no title bar visable)
    welcome_window.wm_attributes('-fullscreen', 'True')
    welcome_window.mainloop()

def create_home_window():
    
    global root #Creates new window
    global tuner_clef
    global training_data
    global training_data_raw
    training_data = []
    training_data_raw = []

    #Allows for Bass Treble and Alto images to appear
    def change_note_image(IMG_Name='staff'):
        global tuner_clef
        image_Note = 'tkinder/Windows/images/'+tuner_clef+'/'+IMG_Name+'.png'
        change_image(image_Note,image1)
       
    root = Toplevel(welcome_window)
    root.title('Tune Your Instrument')
    root.geometry('{}x{}'.format(800, 480)) #Width x Height
    tuner_clef='Bass'

    #set Background
    bg = PhotoImage(file='tkinder/Windows/images/tamu_background2.png')
    my_label = Label(root,image=bg).place(x=0, y=0, relwidth=1, relheight=1)

    #Creates page, buttons, textboxes and header
    create_page(root)                       #1st creates the grid and buttons    
    header = Label(root,text='Tuner',font=("Arial",30,'bold'),bd=4,relief='solid',padx=20,pady=4).grid(row=1,column=2,columnspan=3,pady=8)
    
    #adds in temporary image and text
    my_file = 'tkinder/Windows/images/sample2.png'
    my_image = PhotoImage(file =my_file)
    image1 = Label(root,image=my_image,bd=3,relief='solid')
    image1.grid(row=2,column=3)
    stringbuf = StringVar(root,value=('+/- ' + str(random.randint(0, 99)) + 'cents')) #text is stored in a StringVar object that the label can access by reference
    image_label = Label(root,textvariable=stringbuf,font=("Ludica Console",12,'bold'),width=9,anchor='e',bd=2,relief='solid').grid(row=2,column=4) #label passively gets text from the textvariable
      
    #adds Bass Alto Treble button functionality
    bass_button = Button(root,text='Bass',width=8,pady=5,bg='light green',font=("Arial",17,'bold'),bd=5, relief ='raised', overrelief='sunken',command=lambda:[change_clef('Bass'),change_note_image()])
    bass_button.grid(row=4,column=1,columnspan=2,padx=20,pady=2)
    treble_button = Button(root,text='Treble',width=8,pady=5,bg='light blue',font=("Arial",17,'bold'),bd=5, relief ='raised', overrelief='sunken',command=lambda:[change_clef('Treble'), change_note_image()])
    treble_button.grid(row=4,column=3,padx=20,pady=2)
    alto_button = Button(root,text='Alto',width=8,pady=2,bg='lavender',font=("Arial",17,'bold'),bd=5, relief ='raised', overrelief='sunken',command=lambda:[change_clef('Alto'), change_note_image()])
    alto_button.grid(row=4,column=5,columnspan=2,padx=20,pady=10)

    #Adds Trainer and Stats button functionality
    after_id = StringVar(root,"")
    train_button = Button(root,text='Train',width=12,pady=10, bg='light blue',bd=5, relief ='raised', overrelief='sunken',command=lambda:[root.after_cancel(after_id.get()),root.destroy(),create_trainer_window()])
    train_button.grid(row=5,column=3,padx=20,pady=15)
    stats_button = Button(root,text='Stats',width=12,pady=10,bg='lavender',bd=5, relief ='raised', overrelief='sunken',command=lambda:[root.after_cancel(after_id.get()),root.destroy(),create_stats_window()])
    stats_button.grid(row=5,column=5,columnspan=2,padx=20,pady=15)

    #Function for continuously updating deviation
    def display_deviation():
        value = signal_buf.get()
        note = mm.closest_note(value)
        deviation = mm.cent_deviation(value,note)
        stringbuf.set(( "+" if deviation > 0 else "") + str(round(deviation,1)) + ' cents') #updates to the label's textvariable automatically display on the label
        
        #Automatic Note updating image
        Temp_List=['B4','C4','F4','G4','D4']
        IMG_Name=mm.note_lookup(note,oct=True)
        change_note_image(IMG_Name)
        
        after_id.set(root.after(500, display_deviation)) #recursively call this function in a new thread after 50 ms (non-blocking/responsive infinite loop)
    
    #Run window
    display_deviation() #start the ongoing background function
    root.mainloop()

def create_trainer_window():

    global trainer_window  #Creates new window
    global tuner_clef

    
    #Allows for Bass Treble and Alto images to appear
    def change_actual_image(img_name='staff'):
        global tuner_clef
        image_Note = 'tkinder/Windows/images/'+tuner_clef+'/'+img_name+'.png'
        change_image(image_Note,image_actual)

    def change_target_image(img_name='staff'):
        global tuner_clef
        image_note = 'tkinder/Windows/images/'+tuner_clef+'/'+img_name+'.png'
        change_image(image_note,image_target)
        
    #root = Toplevel(welcome_window)
    trainer_window = Toplevel(welcome_window)
    trainer_window.title('Train Your Skills')
    trainer_window.geometry('{}x{}'.format(800, 480)) #Width x Height
    
    #set Background
    bg = PhotoImage(file='tkinder/Windows/images/tamu_background2.png')
    my_label = Label(trainer_window,image=bg).place(x=0, y=0, relwidth=1, relheight=1)
    
    #Create trainer page with header, buttons and Textboxes
    create_page(trainer_window)                #Create Textboxes
    header = Label(trainer_window,text='Training',font=("Arial",32,'bold'),bd=4,relief='solid',padx=20,pady=4).grid(row=1,column=3,columnspan=1,pady=8)
    
    try_label = Label(trainer_window,text='Try this^',font=("Arial",12,'bold'),bd=2,relief='solid').grid(row=3,column=2,pady=1)
    actual_label = Label(trainer_window,text='We detected^',font=("Arial", 12, 'bold'),bd=2,relief='solid').grid(row=3,column=3,pady=1)
        
    #adds in temporary image and text actual note
    my_file = 'tkinder/Windows/images/train_icon.png'
    my_image = PhotoImage(file =my_file)
    image_actual = Label(trainer_window,image=my_image,bd=3,relief='solid')
    image_actual.grid(row=2,column=3, padx=20)
    stringbuf = StringVar(root,value=('+/- ' + str(random.randint(0, 99)) + 'cents')) #text is stored in a StringVar object that the label can access by reference
    image_label = Label(trainer_window,textvariable=stringbuf,font=("Ludica Console",12,'bold'),width=9,anchor='e',bd=2,relief='solid',padx=15,pady=1).grid(row=2,column=5)
    off_by_label = Label(trainer_window,text='Note off by: ',font=("Arial",10,'bold'),bd=2,relief='solid',padx=2,pady=1).grid(row=2,column=4,padx=5)

    #adds temporary image for target note
    target_file = "tkinder/Windows/images/treble/A4.png"
    target_image = PhotoImage(file=target_file)
    image_target = Label(trainer_window,image=target_image,bd=3,relief='solid',padx=5)
    image_target.grid(row=2,column=2) 
    
    #adds Bass Alto Treble button functionality
    bass_button = Button(trainer_window,text='Bass',width=8,pady=5,bg='light green',font=("Arial",17,'bold'),bd=5, relief ='raised', overrelief='sunken', command=lambda:[change_clef('Bass'), change_actual_image()])
    bass_button.grid(row=4,column=1,columnspan=2,padx=20,pady=10)
    treble_button = Button(trainer_window,text='Treble',width=8,pady=5,bg='light blue',font=("Arial",17,'bold'), bd=5, relief ='raised', overrelief='sunken', command=lambda:[change_clef('Treble'), change_actual_image()])
    treble_button.grid(row=4,column=3,padx=20,pady=10)
    alto_button = Button(trainer_window,text='Alto',width=8,pady=2,bg='lavender',font=("Arial",17,'bold'), bd=5, relief ='raised', overrelief='sunken', command=lambda:[change_clef('Alto'), change_actual_image(2)])
    alto_button.grid(row=4,column=5,columnspan=2,padx=20,pady=10)
    
    #Add button Tuner and Stats functionality
    after_id = StringVar(root,"")
    tuner_button = Button(trainer_window,text='Tuner',width=12,pady=10,bg='light green', bd=5, relief ='raised', overrelief='sunken', command=lambda:[trainer_window.after_cancel(after_id.get()), trainer_window.destroy(), create_home_window()])
    tuner_button.grid(row=5,column=1,columnspan=2,padx=20,pady=15)
    stats_button = Button(trainer_window,text='Stats',width=12,pady=10,bg='lavender', bd=5, relief ='raised', overrelief='sunken', command=lambda:[trainer_window.after_cancel(after_id.get()), trainer_window.destroy(), trainer_window.destroy(),create_stats_window()])
    stats_button.grid(row=5,column=5,columnspan=2,padx=20,pady=15)
    
	#Function for continuously updating deviation
    def display_deviation():
        actual_value = signal_buf.get()
        actual_note = mm.closest_note(actual_value)

        target_value = target_buf.get()
        target_note = mm.closest_note(target_value)

        deviation = mm.cent_deviation(actual_value,target_note)
        stringbuf.set(( "+" if deviation > 0 else "") + str(round(deviation,1)) + ' cents') #updates to the label's textvariable automatically display on the label
        
        if len(training_data) < 20:
            training_data.append(( "+" if deviation > 0 else "") + str(round(deviation,1)) + ' cents')
            training_data_raw.append(deviation) #raw data as float
        
        #Automatic Note updating image
        IMG_Name=mm.note_lookup(actual_note,oct=True)
        change_actual_image(IMG_Name)
        
        if abs(deviation) < 300:
            IMG_Name=mm.note_lookup(target_note,oct=True)
            change_target_image(IMG_Name)

        
        after_id.set(root.after(500, display_deviation)) #recursively call this function in a new thread after 50 ms (non-blocking/responsive infinite loop)
    
    #Run window
    display_deviation() #start the ongoing background function
    trainer_window.mainloop()
       
def create_stats_window():
    
    global stats_window
    
    def display_today_data():
        s = "Today's results:\n\n"
        if len(training_data) == 0:
            s += 'None...\n\n\n\nStart Training!'
        else:
            #create the list of values in string format
            temp = training_data_raw[0:4]
            for item in training_data[0:4]:
                s += (item + '\n') #dont forget s.strip() to remove last new line
            average_deviation_label.configure(text="Average deviation: " + str(round(sum([abs(ele) for ele in temp])/len(temp),1)),bg = 'yellow')
            image_label = Label(stats_window,text='Great Job!',font=("Arial",13,'bold'),bd=1.5,relief='solid').grid(row=2,column=4,columnspan=3)  
        
        data_display_label.configure(text=s.strip(),bg = 'light green')
        
        
        
    def display_week_data():
        s = "This Week's results:\n\n"
        if len(training_data) == 0:
            s += 'None...\n\n\n\nStart Training!'
        else:
            #create the list of values in string format
            temp = training_data_raw[0:7]
            for i in range (0, len(training_data[0:7])): #print(f"{'Left Aligned Text' : <20}")
                s += ('Day ' + str(i + 1) + ": " + training_data[i] + '\n') #dont forget s.strip() to remove last new line
            average_deviation_label.configure(text="Average deviation: " + str(round(sum([abs(ele) for ele in temp])/len(temp),1)),bg = 'yellow')
            image_label = Label(stats_window,text='Great Job!',font=("Arial",13,'bold'),bd=1.5,relief='solid').grid(row=2,column=4,columnspan=3)  
        
        data_display_label.configure(text=s.strip(),bg = 'light blue')
        
        
    def display_month_data():
        s = "This Month's results:\n\n"
        if len(training_data) == 0:
            s += 'None...\n\n\n\nStart Training!'
        else:
            #create the list of values in string format
            temp = training_data_raw[0:10]
            for item in training_data[0:10]:
                s += (item + '\n') #dont forget s.strip() to remove last new line
            average_deviation_label.configure(text="Average deviation: " + str(round(sum([abs(ele) for ele in temp])/len(temp),1)),bg = 'yellow')
            image_label = Label(stats_window,text='Great Job!',font=("Arial",13,'bold'),bd=1.5,relief='solid').grid(row=2,column=4,columnspan=3) 
            
        data_display_label.configure(text=s.strip(),bg = 'lavender')
    
    
    #Allows for Today Week and Month images to appear
    def change_image(pos):
        image_list = ["tkinder/Windows/images/TODAY.png","tkinder/Windows/images/WEEK.png","tkinder/Windows/images/MONTH.png"]
        new_img=ImageTk.PhotoImage(Image.open(image_list[pos]))
        image1.configure(image=new_img)
        image1.image=new_img
        
    #Create the Stats page
    stats_window = Toplevel(welcome_window)
    stats_window.title('Show Your Progress')
    stats_window.geometry('{}x{}'.format(800, 480)) #Width x Height
    
    #set Background
    bg = PhotoImage(file='tkinder/Windows/images/tamu_background2.png')
    my_label = Label(stats_window,image=bg).place(x=0, y=0, relwidth=1, relheight=1)
    
    #Creates page, buttons, and header
    create_page(stats_window)                               #1st creates the grid and button      
    header = Label(stats_window,text='Your Progress',font=("Arial",32,'bold'),bd=4,relief='solid',padx=20,pady=1).grid(row=1,column=3,columnspan=2,pady=8)
    
    #add image
    
    my_file = 'tkinder/Windows/images/stat_icon.png'
    my_image = PhotoImage(file =my_file)
    image1 = Label(stats_window,image=my_image,bd=3,relief='solid')
    image1.grid(row=2,column=3)
    
    #Sets data display box
    data_display_label=Label(stats_window, text="no data yet", font=('Arial 10'),bd=1.5,relief='solid',padx=2,pady=2)
    data_display_label.grid(row=2,column=1,pady=5)
    
    average_deviation_label=Label(stats_window, text="Average: N/A", font=("Helvetica",10,'bold italic'), bd=1.5, relief='solid',padx=3,pady=2)
    average_deviation_label.grid(row=3,column=1,padx=10,pady=1)
    
    #Create Progress Buttons
    b1 = Button(stats_window,text='TODAY',width=8,pady=2,bg='light green',font=("Arial",17,'bold'), bd=5, relief ='raised', overrelief='sunken', command=lambda:[display_today_data(),change_image(0)])
    b1.grid(row=4,column=1,columnspan=2,padx=20,pady=10)
    b2 = Button(stats_window,text='WEEK',width=8,pady=2,bg='light blue',font=("Arial",17,'bold'), bd=5, relief ='raised', overrelief='sunken', command=lambda:[display_week_data(),change_image(1)])
    b2.grid(row=4,column=3,padx=20,pady=10)
    b3 = Button(stats_window,text='MONTH',width=8,pady=2,bg='lavender',font=("Arial",17,'bold'), bd=5, relief ='raised', overrelief='sunken', command=lambda:[display_month_data(),change_image(2)])
    b3.grid(row=4,column=5,columnspan=2,padx=20,pady=10)
    
    #Add Tuner and Trainer Button functionality
    tuner_button = Button(stats_window,text='Tuner',width=12,pady=10, bg='light green', bd=5, relief ='raised', overrelief='sunken', command=lambda:[stats_window.destroy(),create_home_window()])
    tuner_button.grid(row=5,column=1,columnspan=2,padx=20,pady=15)
    trainer_button = Button(stats_window,text='Train',width=12,pady=10, bg='light blue', bd=5, relief ='raised', overrelief='sunken', command=lambda:[stats_window.destroy(),create_trainer_window()])
    trainer_button.grid(row=5,column=3,padx=20,pady=15)
    
    #Run window
    stats_window.mainloop()

#if __name__=="__main__": #only run program immediately if called as a script
    #create_home_window(ProtectedBuffer()) #Start program

if __name__=="__main__": #only run program immediately if called as a script
    create_welcome_window(ProtectedBuffer()) #Start program