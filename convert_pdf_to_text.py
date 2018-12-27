import PyPDF2
import textract

filename="read_file.pdf" 
pdfFileObj=open(filename,'rb')
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
num_pages=pdfReader.numPages
count=0
tex=""

while count<num_pages:
    pageObj=pdfReader.getPage(count)
    count+=1
    tex+=pageObj.extractText()

li=list()
li=tex.splitlines()
tex=""
for t in li:
    tex+=(" "+t)
print(tex)