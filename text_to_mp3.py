import pyttsx3
from gtts import gTTS

engine = pyttsx3.init(driverName='sapi5')
infile = "tanjil.txt"
f = open(infile, 'r')
theText = f.read()
f.close()
tts = gTTS(text=theText, lang='en')
tts.save("saved_file.mp3")
print("File saved!")
