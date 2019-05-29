#from tkinter import ttk
import tkinter

class GridFactory():
    def __init__(self):
        print('factory')
        self.__frames = []

    def build(self, root, columns, rows):
        

        return tkinter.Button(root, text="QUIT", fg="red")
