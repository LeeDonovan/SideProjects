import pygame
from pygame import mixer
from tkinter import *
import os
def playsong():
    currentsong=playlist.get(ACTIVE)
    print("Currently Playing: " ,currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play(fade_ms=10000)# fade in song
def pausesong():
    print("Song has been paused.")
    songstatus.set("Paused")
    mixer.music.pause()
def stopsong():
    print("Song has been stopped.")
    songstatus.set("Stopped")
    mixer.music.fadeout(1000)
def resumesong():
    print("Resuming song: ", playlist.get(ACTIVE))
    songstatus.set("Resuming")
    mixer.music.unpause() 
root=Tk()
root.title('Donovan_s Music Player')
mixer.init()
songstatus=StringVar()
songstatus.set("choosing")
#playlist---------------
playlist=Listbox(root,selectmode=SINGLE,bg="Black",fg="Green",font=('Times',15),width=40)
playlist.grid(columnspan=5)
os.chdir(r'C:\Users\donald\Desktop\Music')#try asking for user input for folder location
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)
playbtn=Button(root,text="Play",command=playsong)
playbtn.config(font=('Times',20),bg="Black",fg="Green",padx=7,pady=7)
playbtn.grid(row=1,column=0)
pausebtn=Button(root,text="Pause",command=pausesong)
pausebtn.config(font=('Times',20),bg="Black",fg="Green",padx=7,pady=7)
pausebtn.grid(row=1,column=1)
stopbtn=Button(root,text="Stop",command=stopsong)
stopbtn.config(font=('Times',20),bg="Black",fg="Green",padx=7,pady=7)
stopbtn.grid(row=1,column=2)
Resumebtn=Button(root,text="Resume",command=resumesong)
Resumebtn.config(font=('Times',20),bg="Black",fg="Green",padx=7,pady=7)
Resumebtn.grid(row=1,column=3)
mainloop()