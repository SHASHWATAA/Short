
from pynput import keyboard

def on_activate():
	print('Global hotkey activated!')
	keyboard.GlobalHotKeys.stop(h)

def on_press(key):
	print('another key {0}'.format(key))



def for_canonical(f):
	return lambda k: f(l.canonical(k))


with keyboard.GlobalHotKeys({'<ctrl>+<alt>+<shift>+<cmd>': on_activate}) as h:
   	h.join()

print('finafuckingly')