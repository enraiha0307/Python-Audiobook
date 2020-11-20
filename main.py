import pyttsx3 
import PyPDF3
book = open('CP_Paper.pdf','rb')
pdfReader = PyPDF3.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()   
for num in range(0,pages):
    page = pdfReader.getPage(0)
    text = page.extractText()
    speaker.setProperty('rate',120)
    speaker.say(text)
    speaker.runAndWait()
