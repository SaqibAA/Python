import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
#pip install pytube
from pytube import YouTube 


#Download Video Function
def DownloadVideo():
    choice = Qualitychoices.get()
    url = urlEntrybox.get()


    if(len(url)<1):
        EbError.config(text="")
        fileError.config(text="")
        MessageQ.config(text="")
        EbError.config(text="Enter URL")
    elif(len(Folder_Name)<1):
        EbError.config(text="")
        fileError.config(text="")
        MessageQ.config(text="")
        fileError.config(text="Please Choose File Location!")
        fileError.grid()
    elif(len(url)>1):
              video = YouTube(url)
       

        if(choice == choices[0]):
            select = video.streams.filter(progressive=True).first()
           

        elif(choice == choices[1]):
            select = video.streams.filter(progressive=True,file_extension='mp4').last()
            

        elif(choice == choices[2]):
            select = video.streams.filter(only_audio=True).first()
            

        else:
            EbError.config(text="")
            fileError.config(text="")
            MessageQ.config(text="Select The Video Quality!")
            
    else:
        EbError.config(text="Enter Valid URL")

        
     #download function       
    select.download(Folder_Name)
    Message.config(text="Download Completed!")


Folder_Name = ""
# Download File Location Function

def selectLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        fileError.config(text="")
        filePath.config(text=Folder_Name,fg="black")
        filePath.grid()
    else:
        filePath.config(text="")
        fileError.config(text="Please Choose File Location!")
        fileError.grid()



    

window=Tk()
 
window.geometry('650x450') # Window Size
window.configure(bg='light green')  # Window  Color
window.columnconfigure(0,weight=1) #set all content in center.
window.title("YouTube Video Downloder")  # Window Title Name




# Window Icon Photo
#window.iconbitmap(r"E:\Blogger\Logo .png")
logo = PhotoImage(file = "E:\Blogger\logo_code_study-removebg-preview.png")
window.iconphoto(False,logo)

 #Application Name Label 
l1=Label(window, text='YouTube Video Downloder', font=(' Bold',40), fg='red', bg='light green')
l1.grid ()

#Horizontal Space
space=Label(window,  bg='light green')
space.grid ()


# URL Label and Entry
l2=Label(window, text='Enter Video URL ', font=('Bold',15), fg='red', bg='light green')
l2.grid ()

videoURL= StringVar()
urlEntrybox = Entry(window,width=50,textvariable=videoURL)
urlEntrybox.grid()

#Entrybox Error Label
EbError = Label(window,text="",bg='light green',font=("Bold",15))
EbError.grid()
#Horizontal Space
space=Label(window,  bg='light green')
space.grid ()


#Path Label and Select path Button
l2=Label(window, text='Select Downloading Path or address', font=('Bold',15), fg='red', bg='light green')
l2.grid ()

btnlocation = Button(window,width=15,bg="grey",fg="white",text="Select Path or File",command=selectLocation)
btnlocation.grid()

#Show File Location Error Label
fileError = Label(window,text="",bg='light green',font=("Bold",10))
fileError.grid()

#Show File Location Label
fileError.config(text="")
filePath = Label(window,text="",bg='light green',font=("Bold",10))
filePath.grid()


#Horizontal Space
space=Label(window,  bg='light green')
space.grid ()



#Download Quality
Quality = Label(window,text="Select Quality",bg='light green',fg='red',font=("Bold",15))
Quality.grid()



#Combobox
choices = ["720p","144p","Only Audio"]
Qualitychoices =ttk.Combobox(window,values=choices)
Qualitychoices.grid()

#Donwload Button
download = Button(window,text="Donwload",width=10,bg="grey",fg="white",command=DownloadVideo)
download.grid()



#Download Message Quality
MessageQ = Label(window,text="",bg='light green',font=("Bold",10))
MessageQ.grid()

#Download Message
Message = Label(window,text="",bg='light green',font=("Bold",25))
Message.grid()

window.mainloop()
