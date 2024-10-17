import customtkinter as ctk
from pytube import YouTube


def  youtube_download():
    try:
        ytube_link = link.get()
        yt_vid = YouTube(ytube_link, on_progress_callback= progress)
        vid = yt_vid.streams.get_highest_resolution()
        label.configure(text= yt_vid.title) #changing the title to the name of the video that is being downloaded
        fin.configure(text= "")
        vid.download()
        fin.configure(text="video successfully downloaded!")
    except:
        fin.configure(text="invalid Youtube link :(", text_color="red")
        
def progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize 
    bytes_downloaded = total_size - bytes_remaining
    percentage = bytes_downloaded/total_size * 100
    per = str(int(percentage))
    progress_perc.configure(text=per + "%")
    progress_perc.update()
    
    #update progress bar
    progress_bar.set(float(percentage/100))
    
    
#app system settings 
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


#app frame
app = ctk.CTk()
app.geometry("720x480")
app.title("YouTube downloader")

#adding UI elements
label = ctk.CTkLabel(app, text="insert a YouTube video link")
label.pack(padx=10, pady=10)

#link input
url = ctk.StringVar()
link = ctk.CTkEntry(app, width=350, height=40, textvariable=url)
link.pack()

#finished downloading
fin = ctk.CTkLabel(app, text="")
fin.pack()

# progress percentage
progress_perc = ctk.CTkLabel(app, text="0%")
progress_perc.pack()

progress_bar = ctk.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

#download button
download = ctk.CTkButton(app, text="Download", command=youtube_download)
download.pack(padx=10,pady=10)

#app run
app.mainloop()


