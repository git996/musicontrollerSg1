#script by git996
import pip
from datetime import datetime

import requests
from time import time,sleep
from pygame import mixer
from random import *
import csv
import webbrowser
import sys
import os
import eyed3

def main():
   install('pygame')
   install('requests')
   install('eyeD3')
   url ="https://musicplayer119.herokuapp.com/index.html"
   urldata = "https://musicplayer119.herokuapp.com/index1.txt"

   webbrowser.open(url,new=0)
   urll.EqWebUrl = requests.get(urldata)
   urll.data  = urll.EqWebUrl.text
   comdata = urll.data.split()

   if comdata[0] == "0":
       urll()
   if comdata[0] == "2":
       urll()
   else:
       reinit()

#installing required packages
def install(package):
     pip.main(['install', package])

def reinit():
   print("Please initialize Tackremote1.0")
   sleep(2)
   urldata = "https://musicplayer119.herokuapp.com/index1.txt"
   urll.EqWebUrl = requests.get(urldata)
   urll.data  = urll.EqWebUrl.text
   comdata = urll.data.split()
   if comdata[0] == "0":
       urll()
   if comdata[0] == "2":
       urll()
   else:
       reinit()

def trackinfo(x):
    af = eyed3.load('C:/Users/New/Music/im/iMusic/song (%d).mp3' % int(x))
    print ('Date: ', af.tag.getBestDate())
    print(af.tag.title,'by ', af.tag.artist)





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
    global comdata
    comdata = urll.data.split()



    if urll.EqWebUrl.status_code == 200:
        print("\nConnected to Remote!")


    if urll.EqWebUrl.status_code != 200:
        print("\nBad Connection!")
    print(comdata[0])



    if comdata[0] == "0":


        print("Track %d selected...waiting for confirmation.."% int(comdata[1]))
        global trackNo
        trackNo = comdata[1]
        #play the track
        music(int(comdata[1]))
        #trank information
        trackinfo(comdata[1])
        mixer.music.set_volume(1.0)


    elif comdata[0] == "1":
        print("Playing  Track %d..... Re-Initialize if not playing!" % int(comdata[1]))
        mixer.music.set_volume(1)
        trackinfo(trackNo)


    if comdata[0] == "2":
        mixer.quit()
        print("Track was Stopped. Player on Stand by...Waiting for Initialization....")


    if comdata[0] == "3":
        mixer.music.pause()
        print("Track Paused")
        trackinfo(trackNo)
    if comdata[0] == "4":
        mixer.music.unpause()
        print("Playing selected track..... Re-Initialize if not Playing!")
        trackinfo(trackNo)


    sleep(2)
    
    urll()
def playTrack(x):
    if x == '1':
        print("Playing  Track %d..... Re-Initialize if not playing!" % int(x[1]))
        mixer.music.set_volume(1)
        trackinfo(trackNo)


if __name__ == "__main__":
    # execute only if run as a script
    main()
