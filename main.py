from pynput import keyboard
from time import time,sleep
import multiprocessing
from subprocess import Popen,PIPE
from pyperclip import paste
import sys
sys.path.append("/Users/shashwataryal/Documents/GIT/Short/")
from Shorthelper import *


def on_press(key):	
	try:
		return (key.char)
		# print('alphanumeric key {0} pressed'.format(key.char))
	except AttributeError:
		pass
		# return (key)
		# print('special key {0} pressed'.format(key))

def on_activate():
	keyboard.GlobalHotKeys.stop(l)


def for_canonical(f):
	return lambda k: f(l.canonical(k))

def logger(key):
	global logTime
	global loggerRan
	global loggedKeys

	runinterval = 0
	if (loggerRan):
		runinterval = time() - logTime
		# print(runinterval)

	logTime = time()
	# print('key was preesed at {0}'.format(logTime))
		
	if (not loggerRan or runinterval < timeBetweenKeys):
		keyPressed = on_press(key)
		loggedKeys = loggedKeys + keyPressed

	loggerRan = True



def bar():
	pass
	

if __name__ == '__main__':
	while True:	
		hotkey = keyboard.HotKey(
			keyboard.HotKey.parse('<ctrl>+<alt>+<shift>+<cmd>'),
			on_activate)

		with keyboard.Listener(
				on_press=for_canonical(hotkey.press),
				on_release=for_canonical(hotkey.release)) as l:
			l.join()
	

		loggedKeys = ''
		loggerRan = False;
		logTime = time()

		timeBetweenKeys = 0.3
		l =  keyboard.Listener(on_press=logger)
		l.start()

		while l.running:
			a =time() - logTime
			if((loggerRan) and (a > timeBetweenKeys)):
				Short(loggedKeys)
				l.stop()







