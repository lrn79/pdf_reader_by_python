import pyttsx3
import PyPDF2

book = open('python.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(book)
page = pdf_reader.numPages
print(page)

friend = pyttsx3.init()
for num in range(0,page):
    pages = pdf_reader.getPage(num)
    text = pages.extractText()
    friend.say(text)
    friend.runAndWait()