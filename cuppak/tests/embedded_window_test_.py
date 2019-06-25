import pytest
import tkinter
from tkinter import messagebox
import cuppak
from cuppak.window import *
from cuppak.component import *
from cuppak.dto import *


def test_run_window():
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

    frame1.add_component('Button', 2, 0, text='An b2', command=cuppakwindow.get_screen_function(1))
    tabframe1 = frame1.add_component('HorizontalTabFrame', 0, 0, component_module='this', fill_frame=True)
    monkiesview = tabframe1.add_tab('Monkies')
    monkiesview.config(bg='#000')
    elephantsview = tabframe1.add_tab('Elephants')
    elephantsview.config(bg='#FFF')
    tiggerview = tabframe1.add_tab('Tiger')
    cowview = tabframe1.add_tab('Cow')

    frame10 = tiggerview.add_component('Frame', 0, 0, component_module='this', fill_frame=True, columns=[ColumnDefinition(1)], rows=[ColumnDefinition(1)])

    slider2 = frame10.add_component('IntegerSliderFrame', 0, 0, component_module='this', fill_frame=True)
    slider2.set_max(200)
    slider2.set_min(-300)
    slider2.set_value(-150)

    print(slider2.get_value())

    frame4 = monkiesview.add_component('Frame', 0, 0, component_module='this', fill_frame=True, columns=columnsa, rows=rowsb, bg='#000')
    frame4.add_component('Button', 0, 0, component_module='ttk', text='ooo ah')


    cmbvalues = ['Some','Values','Here']

    frame7 = elephantsview.add_component('Frame', 0, 0, component_module='this', fill_frame=True, columns=columnsa, rows=rowsb, bg='#CCC')
    combobox = frame7.add_component('ComboboxFrame', 0, 0, component_module='this', fill_frame=True, choices=cmbvalues, state='readonly')
    print(combobox.get_value())

    frame11 = cowview.add_component('Frame', 0, 0, component_module='this', fill_frame=True, columns=[ColumnDefinition(1)], rows=[ColumnDefinition(1)])

    slider2 = frame11.add_component('FloatSliderFrame', 0, 0, component_module='this', fill_frame=True)
    slider2.set_max(200)
    slider2.set_min(-300)
    slider2.set_value(-150)

    screen2.add_component('DynamicLabelFrame', 1, 1,  component_module='this', text='Some words',  image='arrow.png', fill_frame=True, compound='left')
    screen2.add_component('Button', 2, 0, text='Hamster', command=cuppakwindow.get_screen_function(title='screen1'))
    slider = screen2.add_component('IntegerSliderFrame', 0, 1, component_module='this', fill_frame=True)
    slider.set_max(1000)
    slider.set_min(-50)


    screen2.add_component('TextEntryFrame', 2, 1, component_module='this', fill_frame=True)

    screen2.add_component('Button', 0, 0, text='Birb', command=cuppakwindow.get_screen_function(title='screen1'))

    treecolumns = [TreeviewColumnDefinition('one', 'column A', 125), TreeviewColumnDefinition('two', 'column B', 75)]

    treeframe = frame1.add_component('TreeviewFrame', 0, 1, columns=treecolumns, component_module='this', fill_frame=True)

    row1 = TreeviewItemDefinition('The First Line', values=[TreeviewItemValueDefinition('two','2nd'), TreeviewItemValueDefinition('one','1st')])
    treeframe._add_item(row1)

    row2 = TreeviewItemDefinition('The Second Line', values=[TreeviewItemValueDefinition('one','3rd'), TreeviewItemValueDefinition('two','4th')])
    command_a = lambda: print('command fired')
    row3 = TreeviewItemDefinition('Another sub Line', values=[TreeviewItemValueDefinition('two','Dogs'), TreeviewItemValueDefinition('one','Cats')], command=command_a)

    directry = TreeviewDirectoryDefinition('dire','Folder A', items=[row2,row3])
    treeframe._add_directory(directry)

    radio_buttons = [RadioButtonDefinition('abc', 'value1'), RadioButtonDefinition('dfg', 'value2'), RadioButtonDefinition('hij', 'value3')]


    frame1.add_component('HorizontalSelectorFrame', 0, 2,  component_module='this', radio_buttons=radio_buttons, fill_frame=True)

    frame1.add_component('VerticalSelectorFrame', 1, 2,  component_module='this', radio_buttons=radio_buttons, fill_frame=True)

    checkboxa = None

    def getbox():
        print(checkboxa.get_value())

    def randomfunc():
        print('buttontriggered')    

    checkboxa = frame1.add_component('CheckboxFrame', 2, 2,  component_module='this', label='Click', onvalue='Y', offvalue='N', command=getbox, fill_frame=True)
    frame1.add_component('ButtonFrame', 1, 0,  component_module='this', label='Click Me Button', command=randomfunc, image='arrow.png', fill_frame=True, compound='bottom')


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
    txtbx = frame2.add_component('MultilineFrame', 1, 1, component_module='this', fill_frame=True)

    def printtxtbox():
        print(txtbx.get_text())

    frame2.add_component('Button', 1, 2, text='Txt', command=printtxtbox)

    loadsubwindow()
    #cuppakwindow.render()
    assert True

