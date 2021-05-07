from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pyttsx3

FileName = ''


def chooseDir():
    global FileName

    FileName = filedialog.askopenfilename()

    if len(FileName) > 1:
        readFromFileLocation.config(text=FileName, fg='green', font=('Ubuntu', 8, 'bold'), bg='white')

    else:
        messagebox.showerror(title='Location is not selected', message='Try again! select valid location', fg='red')


def textToSpeech():
    userText = textEntry.get("1.0", END)

    if len(FileName) > 1:
        res = messagebox.askyesno(title='Warning',
                                  message='It will stop after reading all your text. Want to continue?')

        if res:
            engine = pyttsx3.init()
            with open(FileName) as f:
                lines = f.read().splitlines()
            engine.setProperty('rate', 115)
            engine.setProperty('volume', 10)
            engine.say(str(lines))
            engine.runAndWait()

        else:
            pass

    elif len(userText) > 1:
        res = messagebox.askyesno(title='Warning',
                                  message='It will stop after reading all your text. Want to continue?')
        if res:
            engine = pyttsx3.init()
            engine.setProperty('rate', 115)
            engine.setProperty('volume', 10)
            engine.say(userText)
            engine.runAndWait()

        else:
            pass
    else:
        messagebox.showerror(title='Empty Text', message='Please enter the text and retry!')


def clearText():
    global FileName
    FileName = ''
    textEntry.delete("1.0", "end")
    readFromFileLocation.config(text='Select File', fg='green',
                                font=('', 10, 'bold'))


window = Tk()
window.geometry('350x500')
window.title('LazZy Reader')
window.resizable(0, 0)

topFrame = Frame(window, width=1000, height=40, bg='light green', bd=20)
topFrame.pack(fill=X, side=TOP)
centerFrame = Frame(window, width=1000, height=300)
centerFrame.pack(fill=X)
bottomFrame = Frame(window, width=1000, height=20, bg='light blue', bd=10)
bottomFrame.pack(fill=X, side=BOTTOM)

topTitle = Label(topFrame, text='BE LAZzy', fg='red', font=('Ubuntu', 18, 'bold'))
topTitle.pack()

readFromTextLabel = Label(centerFrame, text='Play From A Text', fg='black', font=('Ubuntu', 12), bd=5)
readFromTextLabel.pack()

textEntryVar = StringVar()
textEntry = Text(centerFrame, width=40, height=8, wrap=WORD, highlightcolor='red', bd=3)
textEntry.pack()

lineLabel = Label(centerFrame, text='________________________________________________________________________', bd=3)
lineLabel.pack()

readFromFileLabel = Label(centerFrame, text='OR From A File', fg='black', font=('Ubuntu', 12), bd=5)
readFromFileLabel.pack()

lineLabel = Label(centerFrame, text='')
lineLabel.pack()

readFromFileButton = Button(centerFrame, text='Choose File (Only TXT)', activebackground='white',
                            activeforeground='black', bg='black', fg='white', bd=3, relief=GROOVE, command=chooseDir)
readFromFileButton.pack()
readFromFileLocation = Label(centerFrame, text='this is the location of file you selected', fg='green',
                             font=('', 10, 'bold'))
readFromFileLocation.pack()

lineLabel = Label(centerFrame, text='________________________________________________________________________', bd=3)
lineLabel.pack()

lineLabel = Label(centerFrame, text='', bd=3)
lineLabel.pack()

playButton = Button(centerFrame, text='Lets Play', activebackground='white', activeforeground='black', bg='black',
                    fg='white', bd=3, relief=GROOVE, width=20, command=textToSpeech)
playButton.pack(side=LEFT)

clearButton = Button(centerFrame, text='Clear file or text', activebackground='white', activeforeground='black', bg='black',
                     fg='white', bd=3, relief=GROOVE, width=20, command=clearText)
clearButton.pack(side=RIGHT)

window.mainloop()
