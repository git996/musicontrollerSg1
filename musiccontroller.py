#script by git996
import pip
from datetime import datetime
import threading
from threading import Thread
import requests
from time import time,sleep
from pygame import mixer
from random import *
import csv
import webbrowser
import sys
import os
import tweepy
import eyed3
import smtplib


def main():

   dtm = datetime.now()
   global ses
   ses = requests.session()
   global stdtm
   stdtm = str(dtm)

   url ="https://musicplayer119.herokuapp.com/index.html"
   urldata = "https://musicplayer119.herokuapp.com/index1.txt"
   webbrowser.open(url)

   urll.EqWebUrl = ses.get(urldata)
   urll.data  = urll.EqWebUrl.text
   if not urll.EqWebUrl.status_code == 200:
       sleep(20)
       main()
   comdata = urll.data.split()
   print('Printing Result: '+''+comdata[0])

   if comdata[0] == "0":
       urll()

   if comdata[0] == "2":
       Thread(target = urll).start()


   if comdata[0] == "1" or comdata[0] == "3" or comdata[0] == "4":
       reinit()

#installing required packages
def install(package):
     pip.main(['install', package])

def reinit():
   print("Please initialize ----------Tackremote1.0")
   Thread(target = twitter_handle).start()
   sleep(3)
   urldata = "https://musicplayer119.herokuapp.com/index1.txt"
   urll.EqWebUrl = ses.get(urldata)
   urll.data  = urll.EqWebUrl.text
   comdata = urll.data.split()
   if comdata[0] == "0" or comdata[0] == "2":
       Thread(target = urll).start()
       Thread(target = twitter_handle).start()

   else:
       reinit()

def trackinfo(x):
    af = eyed3.load('path/to/song (%d).mp3' % int(x))
    return af.tag.title +' '+'by ' + af.tag.artist +', Year: '+ str(af.tag.getBestDate())





def music(rand):
    mixer.init()
    #rand = randint(1,119)
    url = 'path/to/song (%d).mp3' % rand

    mixer.music.load(url)
    mixer.music.play()
    volume = mixer.music.get_volume()*100
    print("Volume:", volume)


def urll():

    threading.Timer(2.5,urll).start()
    urldata = "https://musicplayer119.herokuapp.com/index1.txt"
    urll.EqWebUrl = ses.get(urldata)
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
        mixer.music.set_volume(0.6)
        message = """Subject: Python Updates
        \nThis is an automated message to let you know that you have fired up an instance of musicplayer119.
        """
        send_mail('xx@gmail.com', message, stdtm)

    elif comdata[0] == "1":
        print("Playing  Track %d..... Re-Initialize if not playing!" % int(comdata[1]))
        mixer.music.set_volume(1)
        print(trackinfo(trackNo))

    if comdata[0] == "2":
        mixer.quit()
        print("Track was Stopped. Player on Stand by...Waiting for Initialization....")


    if comdata[0] == "3":
        mixer.music.pause()
        print("Track Paused")
        print(trackinfo(trackNo))
    if comdata[0] == "4":
        mixer.music.unpause()
        print("Playing selected track..... Re-Initialize if not Playing!")
        print(trackinfo(trackNo))


def twitter_handle():
    twitter_auth()
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = twitter_auth.api.auth, listener=myStreamListener)
    myStream.filter(track=['#musicplayer119'])


def send_mail(toaddrs,msg,x):
    #toaddrs = [toaddrs, 'sushanta1996@gmail.com']
    mg1 = msg +'\nCURRENT TRACK: '+ trackinfo(trackNo)+'\n'+'\nEvent Fired : '+x
    fromaddr = 'xx@gmail.com'
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login("xx@gmail.com", "1234")
    server.sendmail(fromaddr, toaddrs, mg1)
    server.quit()
    print("Message Sent")

def twitter_auth():
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_secret = ''

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token,access_secret)
    twitter_auth.api =  tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, data):
        x = randint(1, 119)
        user1 = data.user
        
        time = data.created_at
        print(data.text)
        print(user1.screen_name)
        music(x)
        trackinfo(x)
        #filesWrite(time,user1.screen_name,data.text)
        print('----------------------------------------------')
        #comdata = data.text.split()
        #if data.text == 'play' or 'Play':





if __name__ == "__main__":
    # execute only if run as a script
    main()
