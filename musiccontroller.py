#script by git996
from datetime import datetime
import requests
from time import time,sleep
from pygame import mixer
from random import *
import csv
import sys

def main():

    
   urll() 


def music(rand):

    mixer.init()
    #rand = randint(1,119) 
    url = 'C:/Users/New/Music/im/iMusic/song (%d).mp3' % rand 
    
    mixer.music.load(url)
    mixer.music.play()
    volume = mixer.music.get_volume()*100
    
        
    print("Volume:", volume)
    
 
def urll():
    
    urldata = "https://musicplayer119.herokuapp.com/index1.txt"
    urll.EqWebUrl = requests.get(urldata)
    urll.data  = urll.EqWebUrl.text
   
    comdata = urll.data.split()
    
    
    if urll.EqWebUrl.status_code == 200: 
        print("Connected to Remote!")
    

    if urll.EqWebUrl.status_code != 200: 
        print("Bad Connection!")
    
 
    if comdata[0] == "0":
        print("Track %d selected...waiting for confirmation.."% int(comdata[1]))
        music(int(comdata[1]))
        mixer.music.set_volume(0.4)
        
       	
    if comdata[0] == "2":
        mixer.quit()    
        print("Track was Stopped. Player on Stand by...Waiting for Initialization....")

    if comdata[0] == "1":
        
        print("Playing  Track %d..... Re-Initialize if not playing!" % int(comdata[1]))
        
        
        mixer.music.set_volume(1)
        #sleep(10)
        #mixer.music.play()
        #mixer.music.queue('C:/Users/New/Music/im/iMusic/song (%d).mp3' % 7)
        #print("Playing Next Track..")
       
        
        
       
        #music()

    if comdata[0] == "3":
        mixer.music.pause()
        print("Track Paused")
    if comdata[0] == "4":
        mixer.music.unpause()
        print("Playing selected track..... Re-Initialize if not Playing!")
    
       
        
        
        
    sleep(1)
    urll()
	
if __name__ == "__main__":
    # execute only if run as a script
    main()
