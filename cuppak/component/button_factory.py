#from tkinter import ttk
import tkinter

class ButtonFactory():
    def __init__(self):
        print('factory')

    def build(self, root):
        button = tkinter.Button(root, text="QUIT", fg="red")
        #button.pack()
        return button