from tkinter import *
from googletrans import Translator

root = Tk()
root.title("Translator")
app_width = 500
app_height = 400
root.geometry(f'{app_width}x{app_height}+{250}+{250}')

my_l = Label(root, text="Enter Name in English: ", bg="gray")
my_l.pack(pady=10)

e = Entry(root, width=35, borderwidth=5)
e.pack(pady=10)

myButton = Button(root, text="Enter Name in English: ", command=e.get())


def myDelete():
    e1.destroy()
    myButton['state'] = NORMAL


def transalator():
    global e1
    translator = Translator()
    translation = translator.translate(e.get(), dest="ar")
    my_text = StringVar()
    my_text.set(translation.text)
    e1 = Entry(root, font=("Helvetica", 20), borderwidth=5, bd=0, state="readonly", textvariable=my_text, fg="blue")
    e1.pack(pady=10)
    e.delete(0, 'end')
    myButton['state'] = DISABLED
    # print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


myButton = Button(root, text="Translate", fg="Red", command=transalator)
myButton.pack(pady=10)

DeleteButton = Button(root, text="Clear Text", command=myDelete)
DeleteButton.pack(pady=10)

root.mainloop()
