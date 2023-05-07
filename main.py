import PyPDF2
import pyttsx3


def pdfread():
    file_path = input("Enter the pdf path : ")
    path = open(file_path, 'rb')
    pdfReader = PyPDF2.PdfReader(path)
    start = int(input("Enter start page : "))
    close = int(input("Enter the end page : "))
    speed = int(input("Enter speed \n1=1x,2=2x,3=3x...: "))
    text = ""

    for i in range(start-1, close):
        page = pdfReader.pages[i]
        text += page.extract_text()

    speak = pyttsx3.init()
    speak.setProperty('rate', speed*100)
    speak.say(text)
    speak.runAndWait()


pdfread()
