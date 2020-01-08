# -*- coding utf-8 -*-
from threading import Thread
from tkinter import *
from tkinter import ttk
import functools


class main_Window:
    def __init__(self):
        clientWindow = Tk()
        Label(clientWindow, text='Welcome to Tk!').grid(row=0)
        Label(clientWindow, text='IP').grid(row=1)
        Label(clientWindow, text='PORT').grid(row=2)
        e1=Entry().grid(row=1, column=1)
        e2=Entry().grid(row=2, column=1)
        print_it=functools.partial(main_Window.print_word,'ok')
        ttk.Button(clientWindow,text='ok',command=print_it).grid(row=3)


        clientWindow.mainloop()
    def getUserHost(self):
        IP=main_Window.e1.get()
        PORT=main_Window.e2.get()
        HOST=(IP,PORT)
        return HOST
    @classmethod
    def print_word(cls,word):
        print(word)


class canvas_demo(main_Window,Thread):
    def __init__(self):
        main_Window.__init__()
        Thread.__init__()
        window=main_Window()
        cv=Canvas(window,bg='white')
        cv.pack



if __name__ == '__main__':
    window=main_Window()
    HOST=window.getUserHost()
    print(HOST)




