from gtts import gTTS
with open("tanjil.txt",'r') as infile:
    tts = gTTS(text=infile.read(), lang='en')
    tts.save("saved_file.mp3")
    print("File saved!")
