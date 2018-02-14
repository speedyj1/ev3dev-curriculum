"""
This is the tkinter side of the code.
"""


import tkinter
from tkinter import ttk


def main():

    window1link()






def window1link():
    root = tkinter.Tk()  # makes window

    window1 = ttk.Frame(root, padding=20)
    window1.grid()

    button_1 = ttk.Button(window1, text='Button 1')
    button_1.grid(row=0, column=0)
    button_1['command'] = lambda: window2link()

    button_2 = ttk.Button(window1, text='Button 2')
    button_2.grid(row=1, column=0)
    button_2['command'] = lambda: window3link()

    button_3 = ttk.Button(window1, text='Button 3')
    button_3.grid(row=2, column=0)

    button_4 = ttk.Button(window1, text='Button 4')
    button_4.grid(row=3, column=0)

    root.mainloop()

def window2link():
    root = tkinter.Tk()  # makes window

    window2 = ttk.Frame(root, padding=20)
    window2.grid()

    root.mainloop()

def window3link():
    root = tkinter.Tk()  # makes window

    window3 = ttk.Frame(root, padding=20)
    window3.grid()

    root.mainloop()









main()