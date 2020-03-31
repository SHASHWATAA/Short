import os
from subprocess import Popen,PIPE,call
from pyperclip import paste
from datetime import datetime
from tkinter import filedialog,Tk
from pathlib import Path

def Short(keyPressed):
	log(keyPressed)

	function_dictionary = {
	'fo':openFolderFromClipboard,
	'ft':openFinderInTerminal,
	'e':openEncoderCurrentDir
	}

	try:
		function_dictionary[keyPressed]()
	except KeyError:
		print('\a')



def openFolderFromClipboard():
	#to-do error handling
	directory = paste()
	# print(directory)
	call(["open",directory])

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
	call(['/Users/shashwataryal/Documents/Python/Transcoder for TV/encoder run from short.py'])





