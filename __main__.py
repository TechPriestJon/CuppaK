#from io.iowindow import IOWindow
#import cuppak.window.window
#from baconsarnie.io.window import Window
from cuppak.window import *

from cuppak.component import *

import tkinter
#from baconsarnie import Window

##print( help('modules'))
print('run')
###cuppakwindow = BasicWindow(800, 600, 'CuppaK')
###cuppakwindow.add_component(ButtonFactory())
###cuppakwindow.render()

#columns = [ColumnDefinition(2), ColumnDefinition(1), ColumnDefinition(4)]

#rows = [RowDefinition(1), RowDefinition(2)]

#cuppakwindow = GridWindow(800, 600, 'CuppaK', columns, rows)
###cuppakwindow.add_grid(WeightGridFactory(), columns, rows)
#cuppakwindow.add_component(ButtonFactory(), 1, 1)
#cuppakwindow.add_component(ButtonFactory(), 2, 0)
#cuppakwindow.add_component(ButtonFactory(), 0, 0)

cuppakwindow = Window(800, 600, 'CuppaK Anuva Cuppa')

screen1 =  cuppakwindow.add_screen([ColumnDefinition(2), ColumnDefinition(1)], [RowDefinition(1)], 'screen1')
screen2 = cuppakwindow.add_screen([ColumnDefinition(2), ColumnDefinition(1), ColumnDefinition(4)], [RowDefinition(1), RowDefinition(2)], 'screen2')

#screen1 = Screen(cuppakwindow, )
#screen2 = Screen(cuppakwindow, [ColumnDefinition(2), ColumnDefinition(1), ColumnDefinition(4)], [RowDefinition(1), RowDefinition(2)])
#screen3 = Screen(cuppakwindow, )


buttoninst = getattr(tkinter, 'Button')

buttona = buttoninst(screen1, text='Dog', command=cuppakwindow.get_screen_function(1))
buttonb = tkinter.Button(screen1, text='Cat', command=cuppakwindow.get_screen_function(1))
buttonc = tkinter.Button(screen2, text='Cat', command=cuppakwindow.get_screen_function(0))
buttond = tkinter.Button(screen2, text='Hamster', command=cuppakwindow.get_screen_function(0))
buttone = tkinter.Button(screen2, text='Birb', command=cuppakwindow.get_screen_function(0))

menu = tkinter.Menu(cuppakwindow)
menu.add_command(label="Page1", command=cuppakwindow.get_screen_function(0))
menu.add_command(label="Page2", command=cuppakwindow.get_screen_function(1))
screen1.add_menu(menu)

screen1.add_component_type('Button', 0, 0, text='Dog2', command=cuppakwindow.get_screen_function(1))
screen1.add_component(buttonb, 1, 0)
screen2.add_component(buttonc, 1, 1)
screen2.add_component(buttond, 2, 0)
screen2.add_component(buttone, 0, 0)

cuppakwindow.load_screen(0, 'screen1')

screen3 = screen1.spawn_subwindow([ColumnDefinition(2), ColumnDefinition(1), ColumnDefinition(4)], [RowDefinition(1), RowDefinition(2)], 'subwindow')

screen3.add_component_type('Button', 1, 1, text='An b1')
screen3.add_component_type('Button', 2, 0, text='An b2')
screen3.add_component_type('Button', 0, 0, text='An b3')


cuppakwindow.render()
print('complete')

