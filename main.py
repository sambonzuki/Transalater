from tkinter import*
from translate import  Translator
root = Tk()
root.geometry("300x300")
root.title("Language translator voice bot")
inputlanguage = StringVar()
outputlanguage = StringVar()
languagechoices = {'English', 'Spanish', 'Chinese', 'Ukrainian', 'Finnish', 'Hungarian', 'Belgian', 'Polish'}
inputlanguage.set('English')
outputlanguage.set('Chinese')
def Translate():
    translator = Translator(from_lang = inputlanguage.get(), to_lang = outputlanguage.get())
    translation = translator.translate(TextVar)
canvas = Canvas(root, height=100, width=100)
canvas.pack()
label = Label(root, text="Chose your language", height=10, width=15)
label.pack(side=LEFT, pady=15)
label1 = Label(root, text="French", height=10, width=15)
label1.pack(side=LEFT, pady=15)
label.pack()
root.mainloop()
