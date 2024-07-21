import PyPDF2
import pdfplumber
import pyttsx3 as tts
from tkinter import *
from tkinter.filedialog import askopenfilename

root = Tk()
root.geometry("600x300")
root["bg"] = "skyblue"

root.title("Pdf to AudioFile")


def upload_file():
    file = askopenfilename()
    f = open(file, "rb")
    pdf_reader = PyPDF2.PdfReader(f)
    pages = pdf_reader.pages
    text = ""

    with pdfplumber.open(file) as pdf:
        for i in range(len(pages)):
            page = pdf.pages[i]
            text += page.extract_text()
            print(text)

    engine = tts.init()
    engine.setProperty("rate", 150)
    engine.save_to_file(text, "audio.mp3")
    engine.runAndWait()
    info_label = Label(text="DOWNLOADED\nOpen 'audio.mp3' file to listen.", font=("Arial", 18), bg="skyblue")
    info_label.pack(pady=50)


title_label = Label(text="Choose a pdf file to convert", font=("Arial", 18), bg="skyblue")
title_label.pack(pady=30)

upload_file_button = Button(text="Upload File", command=upload_file, bg="lightblue")
upload_file_button.pack()

root.mainloop()