import os
from subprocess import Popen,PIPE,call
from pyperclip import paste
from datetime import datetime
from tkinter import filedialog,Tk
from pathlib import Path
from playsound import playsound
from pyautogui import typewrite
import pyperclip

def Short(keyPressed):
	log(keyPressed)

	function_dictionary = {
	'cf':openFolderFromClipboard,
	'cc':copyClipboardtoChrome,
	'ct':copyClipboardtoTerminal,
	'g':openGarageband,
	'ft':openFinderInTerminal,
	'e':openEncoderCurrentDir,
	's':openSpotifyApp,
	'm':openMessenger,
	'z':loginZoom,
	'v':fakePaste
	}

	try:
		function_dictionary[keyPressed]()
		# playsound("/Users/shashwataryal/Documents/GIT/Short/success.wav")
	except KeyError:
		playsound("/Users/shashwataryal/Documents/GIT/Short/error.aifc")



def openFolderFromClipboard():
	#to-do error handling
	directory = paste()
	# print(directory)
	call(["open",directory])


def copyClipboardtoChrome():
	#to-do error handling
	url = paste()
	# print(directory)
	os.system('open -n -a "Google Chrome" --args --profile-directory=Default "{0}" &'.format(url))

def copyClipboardtoTerminal():
	# #to-do error handling
	# command = paste()
	# # print(directory)
	# os.ctsystem(command)
	a = 1

def openGarageband():
	os.system('open "/Applications/GarageBand.app" &')



def openFinderInTerminal():

	script = '''
				tell application "Finder" to set currentDir to POSIX path of (insertion location as alias)
				tell application "Terminal"
					do script "cd '" & currentDir & "'"
					activate
				end tell
			'''

	p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE,universal_newlines=True)
	stdout, stderr = p.communicate(script)

def log(keyPressed):
	a = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	f= open("/Users/shashwataryal/Documents/GIT/Short/log.txt","a")
	f.write(a + ' ' + keyPressed + '\n' )

def openEncoderCurrentDir():
	os.system('python3 "/Users/shashwataryal/Documents/Python/Transcoder for TV/encoder run from short.py" &')
	# os.system('sleep 5 &')
	print("done")


def openSpotifyApp():
	os.system('open "/Users/shashwataryal/Applications/Chrome Apps.localized/Spotify.app" &')
	print("done")


def openMessenger():
	# os.system('open -n -a "Google Chrome" --args --profile-directory=Default "http://messenger.com/" &')
	os.system('open /Applications/Messenger.app &')


def addNewShortHelper():
	os.system('launchctl unload "/Users/shashwataryal/Library/LaunchAgents/com.shashwat.short.plist"; open "/Users/shashwataryal/Documents/GIT/Short/Shorthelper.py"; cd "/Users/shashwataryal/Documents/GIT/Short/"; python3 "main.py"')

def doneDoneLoadShortDeamon():
	os.system('launchctl load "/Users/shashwataryal/Library/LaunchAgents/com.shashwat.short.plist"')




def loginZoom():
	os.system('python3 "/Users/shashwataryal/Documents/Python/Open Zoom/main.py" &')
	# os.system('sleep 5 &')
	print("done")

def fakePaste():
	clipboard = pyperclip.paste()
	typewrite(clipboard)

	