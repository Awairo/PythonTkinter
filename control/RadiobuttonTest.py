

from Tkinter import *

root = Tk()
#root.option_readfile('optiondB')
root.title('Toplevel')
#root.geometry('400x300')

var = IntVar()
for text, value in [('Passion fruit', 1), ('Loganberries', 2),
                    ('Mangoes in syrup', 3), ('Oranges', 4),
                    ('Apples', 5), ('Grapefruit', 6)]:
    #Radiobutton(root, text=text, value=value, variable=var).pack(anchor=W)
    Radiobutton(root, text=text, value=value, variable=var, indicatoron=0).pack(
        anchor=W, fill=X, ipadx=18)
var.set(3)

root.mainloop()