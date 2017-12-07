

from Tkinter import *

root = Tk()
#root.option_readfile('optiondB')
root.title('Toplevel')
#root.geometry('400x300')

Label(root, text="Anagram").pack(side=LEFT, padx=5, pady=10)
e = StringVar()
Entry(root, width=40, textvariable=e).pack(side=LEFT)
e.set("'A shroe! A shroe! My dingkom for a shroe!'")

root.mainloop()