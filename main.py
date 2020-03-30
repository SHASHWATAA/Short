from pynput import keyboard
from time import time
import multiprocessing
from subprocess import call,Popen,PIPE
from pyperclip import paste
import sys
sys.path.append("/Users/shashwataryal/Documents/GIT/Short/")

from Sfthorthelper import *


class MyException(Exception): pass

def on_press(key):	
	try:
		return (key.char)
		# print('alphanumeric key {0} pressed'.format(key.char))
	except AttributeError:
		return (key)
		# print('special key {0} pressed'.format(key))

def on_activate():
	print('Global hotkey activated!')
	raise MyException()


def for_canonical(f):
	return lambda k: f(l.canonical(k))

def logger(key):
	global logTime
	global loggerRan
	global loggedKeys

	runinterval = 0
	if (loggerRan):
		runinterval = time() - logTime
		print(runinterval)

	logTime = time()
	print('key was preesed at {0}'.format(logTime))
		
	if (not loggerRan or runinterval < timeBetweenKeys):
		keyPressed = on_press(key)
		loggedKeys = loggedKeys + keyPressed

	loggerRan = True


def bar():
	listener.join()

if __name__ == '__main__':
	while True:	
		hotkey = keyboard.HotKey(
			keyboard.HotKey.parse('<ctrl>+<alt>+<shift>+<cmd>'),
			on_activate)

		with keyboard.Listener(
				on_press=for_canonical(hotkey.press),
				on_release=for_canonical(hotkey.release)) as l:
			try:
				l.join()
			except MyException as e:
				print("success!")		

		loggedKeys = ''
		loggerRan = False;
		logTime = time()

		timeBetweenKeys = 0.3
		listener = keyboard.Listener(on_press=logger)
		listener.start()
		p = multiprocessing.Process(target=bar)
		p.start()

		while p.is_alive():
			# print ("running...")
			a =time() - logTime
			print(a, loggerRan)
			if((loggerRan) and (a > timeBetweenKeys)):
				Short(loggedKeys)
				p.terminate()
				p.join()
				listener.stop()







