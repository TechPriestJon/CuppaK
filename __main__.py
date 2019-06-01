#from io.iowindow import IOWindow
#import cuppak.window.window
#from baconsarnie.io.window import Window
from cuppak.window import *

from cuppak.component import *
#from baconsarnie import Window

#print( help('modules'))
print('run')
##cuppakwindow = BasicWindow(800, 600, 'CuppaK')
##cuppakwindow.add_component(ButtonFactory())
##cuppakwindow.render()

columns = [ColumnDefinition(2), ColumnDefinition(1), ColumnDefinition(4)]

rows = [RowDefinition(1), RowDefinition(2)]

cuppakwindow = GridWindow(800, 600, 'CuppaK', columns, rows)
#cuppakwindow.add_grid(WeightGridFactory(), columns, rows)
cuppakwindow.add_component(ButtonFactory(), 1, 1)
cuppakwindow.add_component(ButtonFactory(), 2, 0)
cuppakwindow.add_component(ButtonFactory(), 0, 0)
cuppakwindow.render()
print('complete')

