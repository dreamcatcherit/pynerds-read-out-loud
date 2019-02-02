import os
from gtts import gTTS
import PyPDF2
import textract
import click

@click.command()
@click.option("--pdf_name",prompt=True)

def convert_pdf_to_text(pdf_name):
    
    """ Converts Portable Document File(PDF) into Text File.
    Parameters: 
        pdf_name(str): The pdf file which is to be converted into text.
    
    Returns:
        This Function returns text file name.
    
    """

    pdf_file_obj=open(pdf_name+".pdf",'rb')
    pdf_reader=PyPDF2.PdfFileReader(pdf_file_obj)
    num_pages=pdf_reader.numPages
    count,text=0,""

    while count<num_pages:
        page_obj=pdf_reader.getPage(count)
        count+=1
        text+=page_obj.extractText()

    list_of_text=list(text.splitlines())

    text_file_name=pdf_name

    with open(text_file_name+".txt","w") as file_pointer:
        for text_from_list in list_of_text:
            file_pointer.write(text_from_list+" ")
    return text_file_name

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
    text_to_audio(convert_pdf_to_text())
