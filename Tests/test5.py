from pynput import keyboard
class MyException(Exception): pass

def on_press(key):
	try:
		print('alphanumeric key {0} pressed'.format(key.char))
	except AttributeError:
		print('special key {0} pressed'.format(key))

	return False

def on_activate():
	print('Global hotkey activated!')
	raise MyException()


def for_canonical(f):
	return lambda k: f(l.canonical(k))

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

with keyboard.Listener(
		on_press=on_press) as listener:
	listener.join()	
