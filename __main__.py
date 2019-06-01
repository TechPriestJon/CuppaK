#from io.iowindow import IOWindow
#import cuppak.window.window
#from baconsarnie.io.window import Window
from cuppak.window import *

from cuppak.component import *
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
screen1 = Screen(cuppakwindow, [ColumnDefinition(2), ColumnDefinition(1)], [RowDefinition(1)])
screen2 = Screen(cuppakwindow, [ColumnDefinition(2), ColumnDefinition(1), ColumnDefinition(4)], [RowDefinition(1), RowDefinition(2)])

screen1.add_component(ButtonFactory('Dog', cuppakwindow.get_screen_function(1)), 0, 0)
screen1.add_component(ButtonFactory('Cat', cuppakwindow.get_screen_function(1)), 1, 0)
screen2.add_component(ButtonFactory('Cat', cuppakwindow.get_screen_function(0)), 1, 1)
screen2.add_component(ButtonFactory('Hamster', cuppakwindow.get_screen_function(0)), 2, 0)
screen2.add_component(ButtonFactory('Birb', cuppakwindow.get_screen_function(0)), 0, 0)

cuppakwindow.add_screen(screen1, 'screen1')
cuppakwindow.add_screen(screen2, 'screen2')
cuppakwindow.load_screen(0, 'screen1')


cuppakwindow.render()
print('complete')

