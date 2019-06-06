
from cuppak.window import *
from cuppak.component import *

import tkinter
from tkinter import messagebox

print('run')

cuppakwindow = Window('CuppaK Anuva Cuppa', 800, 600, False)

screen1 =  cuppakwindow.add_screen([ColumnDefinition(2), ColumnDefinition(1)], [RowDefinition(1)], 'screen1')
screen2 = cuppakwindow.add_screen([ColumnDefinition(2), ColumnDefinition(1), ColumnDefinition(4)], [RowDefinition(1), RowDefinition(2)], 'screen2', background='#DDD')

menu = tkinter.Menu(cuppakwindow)
menu.add_command(label="Page1", command=cuppakwindow.get_screen_function(0))
menu.add_command(label="Page2", command=cuppakwindow.get_screen_function(1))
screen1.add_menu(menu)

columnsa = [ColumnDefinition(2), ColumnDefinition(4), ColumnDefinition(1)]
rowsb = [RowDefinition(1), RowDefinition(2), RowDefinition(1)]

frame1 = screen1.add_component('Frame', 1, 0, component_module='this', fill_frame=True, columns=columnsa, rows=rowsb, background='#FFF')

frame1.add_component('Entry', 1, 1)
frame1.add_component('Button', 2, 0, text='An b2', command=cuppakwindow.get_screen_function(1))
frame1.add_component('Button', 0, 0, text='An b3', command=cuppakwindow.get_screen_function(1))

screen2.add_component('Button', 1, 1, text='Cat', command=cuppakwindow.get_screen_function(0))
screen2.add_component('Button', 2, 0, text='Hamster', command=cuppakwindow.get_screen_function(title='screen1'))
screen2.add_component('Button', 0, 0, text='Birb', command=cuppakwindow.get_screen_function(title='screen1'))

def loadsubwindow():
    columns = [ColumnDefinition(2), ColumnDefinition(1), ColumnDefinition(4)]
    rows = [RowDefinition(1), RowDefinition(2)]

    def on_closing():
        return messagebox.askokcancel("Quit", "Do you want to escape and run away?")
        #return messagebox.askyesnocancel("Quit", "Do you want to escape and run away?")

    subwindow = screen1.spawn_subwindow('subwindow', 400, 200, False, True, on_closing)

    screen3 = subwindow.add_screen(columns, rows, 'screen2')

    screen3.add_component('Button', 1, 1, text='An b1')
    screen3.add_component('Button', 2, 0, text='An b2')
    screen3.add_component('Button', 0, 0, text='An b3')


frame2 = screen1.add_component('Frame', 0, 0, component_module='this', fill_frame=True, columns=columnsa, rows=rowsb, background='#000')

frame2.add_component('Button', 0, 0, text='Dog2', command=loadsubwindow)
txtbx = frame2.add_component('Multiline', 1, 1, component_module='this', fill_frame=True)

def printtxtbox():
    print(txtbx.get_text())

frame2.add_component('Button', 1, 2, text='Txt', command=printtxtbox)

cuppakwindow.render()
print('complete')

