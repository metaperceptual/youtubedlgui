from tkinter import *
from tkinter import filedialog
import subprocess


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Tunes Getter")

        self.label = Label(master, text="Paste Url, Press Get Tunes")
        self.label.pack()

        self.urlentry = StringVar()
        self.url = Entry(self.master,textvariable=self.urlentry)
        self.url.pack()

        self.get_button = Button(master, text="Get Tunes", command=self.getmusic)
        self.get_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

       

    def getmusic(self):
        self.sourceFolder =  filedialog.askdirectory(parent=root, initialdir= "/", title='Please select a directory')
        ytdl="youtube-dl -o \"" + self.sourceFolder + "/%(title)s.%(ext)s\" " + "--metadata-from-title \"%(artist)s - %(title)s\" --extract-audio --add-metadata -f bestaudio -x --audio-format mp3 --audio-quality 0 --embed-thumbnail  -i -c " + self.url.get()
        subprocess.call(ytdl, shell=True)



root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

