
from Tkinter import *

import Pmw

class SLabel(Frame):
    def __init__(self, master, leftl, rightl):
        Frame.__init__(self, master, basestring='gray40')
        self.pack(side=LEFT, expand=YES, fill=BOTH)
        Label(self, text=rightl, fg='steelblue1', 
              font=("arial", 6, "bold"), width=5, bg='gray40').pack(
                  side=LEFT, expand=YES, fill=BOTH)
        Label(self, Text=rightl, fg='white',
              font=("arial", 6, "bold"), width=1, bg='gray40').pack(
                  side=RIGHT, expand=YES, fill=BOTH)

class Key(Button):
    def __init__(self, master, font=('arial', 8, 'bold'),
                 fg='white', width=5, borderwidth=5, **kw):
        kw['font'] = font
        kw['fg'] = fg
        kw['width'] = width
        kw['borderwidth'] = borderwidth
        apply(Button.__init__, (self, master), kw)
        self.pack(side=LEFT, expand=NO, fill=NONE)

class Calculator(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, bg='gray40')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Tkinter Toolkit TT-42')
        self.master.iconname('Tk-42')
        self.calc = Evaluator()

    def doThis(self, action):
        print '"%s" has not been implemented' % action

    def turnoff(self, *args):
        self.quit()

    def clearall(self, *args):
        self.current = ""
        self.display.componet('text').delete(1.0, END)

    def doEnter(self, *args):
        self.focus_displayof.insert(END, '\n')
        result = self.calc.runpython(self.current)
        if result:
            self.focus_displayof.insert(END, '%s\n' % result, 'ans')
        self.current = ""
