#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python37

from keyboard import add_word_listener,wait
from time import sleep

f= open("/Users/shashwataryal/Documents/GIT/Short/test.txt","w+")

def openFolderFromClipboard():
	#to-do error handling
	from subprocess import call
	from pyperclip import paste
	directory = paste()
	print(directory)
	call(["open",directory])

def openFinderInTerminal():
	from subprocess import Popen,PIPE
	script = '''
				tell application "Finder" to set currentDir to POSIX path of (insertion location as alias)
				tell application "Terminal"
					do script "cd '" & currentDir & "'"
					activate
				end tell
			'''

	p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE,universal_newlines=True)
	stdout, stderr = p.communicate(script)

	



add_word_listener('of',openFolderFromClipboard, triggers=['space'])	
add_word_listener('ft',openFinderInTerminal, triggers=['space'])


wait('space')

sleep(0.5)