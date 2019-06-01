#from tkinter import ttk
import tkinter

class ButtonFactory():
    def __init__(self, title, command):
        self.__title = title
        self.__command = command
        print('factory')

    def build(self, root):
        button = tkinter.Button(root, text=self.__title, command=self.__command)
        #button.pack()
        return button