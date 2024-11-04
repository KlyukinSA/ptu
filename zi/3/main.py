from pynput import keyboard
from datetime import datetime

def get_time():
    return str(datetime.now())

def on_press(key):
    try:
        f.write('{0} down {1}\n'.format(get_time(), key.char))
    except AttributeError:
        f.write('{0} down2 {1}\n'.format(get_time(), key))

def on_release(key):
    f.write('{0} release {1}\n'.format(get_time(), key))
    if key == keyboard.Key.esc:
        return False

f = open("log.txt", "w")
f.write("Program start at " + get_time() + '\n')
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
f.write("Program stop at " + get_time() + '\n')
f.close()
