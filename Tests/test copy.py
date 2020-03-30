from pynput import keyboard
from time import time
import multiprocessing


def on_press(key):	
	try:
		return (key.char)
		# print('alphanumeric key {0} pressed'.format(key.char))
	except AttributeError:
		return (key)
		# print('special key {0} pressed'.format(key))

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
		print(loggedKeys)
		p.terminate()
		p.join()

