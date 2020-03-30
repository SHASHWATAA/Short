
from keyboard import add_word_listener,wait,_pressed_events,hook,unhook_all,is_pressed
from subprocess import call,Popen,PIPE
from pyperclip import paste
from time import sleep
import threading

def main():
	print("inmain")
	while  (not(is_pressed('enter'))):
		add_word_listener('of',openFolderFromClipboard, triggers=['enter'])	
		add_word_listener('ft',openFinderInTerminal, triggers=['enter'])
		sleep(1)

	print('waited space')

def openFolderFromClipboard():
	#to-do error handling
	print('of')
	directory = paste()
	print(directory)
	call(["open",directory])

def openFinderInTerminal():
	print('ft')
	script = '''
				tell application "Finder" to set currentDir to POSIX path of (insertion location as alias)
				tell application "Terminal"
					do script "cd '" & currentDir & "'"
					activate
				end tell
			'''

	p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE,universal_newlines=True)
	stdout, stderr = p.communicate(script)


def print_pressed_keys(e):

	line = ', '.join(str(code) for code in _pressed_events)
	print(line)
	if (line == '55, 59, 58, 56, 1'):
		f= open("/Users/shashwataryal/Documents/GIT/Short/test.txt","w+")
		print("yes")
		unhook_all()
		main()




hook(print_pressed_keys)
print("hookpass")



wait('enter')
sleep(1)