from pypdf import PdfReader
import pyttsx3
read = pyttsx3.init()
import pyttsx3

read.setProperty('voice', 'english+f3')
read.setProperty('rate', 147)
read.setProperty()


location = str(input("Enter th location of Pdf: "))
tgt = PdfReader(location)

lenth = len(tgt.pages)
print(f"Total no of pages = {lenth}")

choice = int(input("\nEnter yout choice\n1-> Read whole pdf\n2-> Read specific page\n"))

def read_pdf(n):
    page = tgt.pages[n]
    text = page.extract_text()
    read.say(text)

if(choice == 1):
    for i in range (lenth):
        read_pdf(i)
if(choice == 2):  
    n = int(input("Enter the no of page = "))
    if(n>4 and n<1):
        print("No page available")
    read_pdf(n-1)
read.runAndWait()
read.stop()
