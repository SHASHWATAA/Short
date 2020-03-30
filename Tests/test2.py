
from keyboard import add_word_listener,wait,remove_word_listener
from subprocess import call,Popen,PIPE
from pyperclip import paste
from pynput import keyboard

def main():
	print("inmain")
	add_word_listener('of',openFolderFromClipboard, triggers=['space'])	
	add_word_listener('ft',openFinderInTerminal, triggers=['space'])
	wait('space')
	print('waited space')
	remove_word_listener('of')
	remove_word_listener('ft')

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



if (False):
	f= open("/Users/shashwataryal/Documents/GIT/Short/xxtest.txt","w+")
	print("yes")
	unhook_all()


# The key combination to check
COMBINATION = {keyboard.KeyCode.from_char('s'), keyboard.Key.shift, keyboard.Key.alt, keyboard.Key.ctrl, keyboard.Key.cmd}

# The currently active modifiers
current = set()


def on_press(key):
    if key in COMBINATION:
        current.add(key)
        if all(k in current for k in COMBINATION):
            print('All modifiers active!')
            main()
    if key == keyboard.Key.esc:
        listener.stop()


def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()