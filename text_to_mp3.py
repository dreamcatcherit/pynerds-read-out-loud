import os
from gtts import gTTS
def text_to_audio(text_file):
    '''
    Function:
      Convert text files into mp3 files
    
    Param arg:
      The text file which is to be converted into mp3
      
    Type arg:str
        
    Vartype arg:str
      
    Returns:
      This function doesn't return anything
      
    '''
    filename,extension=os.path.splitext(text_file)
    if (extension=='.txt'):
        with open(text_file,'r') as f:
            tts = gTTS(text=f.read(), lang='en')
            tts.save(filename+".mp3")
if __name__ == "__main__":
    text_to_audio("convert_pdf_to_text.txt")
        
