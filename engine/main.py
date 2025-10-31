import os 
import eel

eel.init('www')

os.system('start chrome.exe --aap="http://localhost:8000/voice.html"')

eel.start('voice.html', mode='chrome', host='localhost', block=True)