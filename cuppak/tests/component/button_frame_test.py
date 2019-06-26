import pytest
from cuppak.component import *
import os

def test_button_frame_type():
    button = ButtonFrame(None, 'Test Button')
    assert str(type(button)) == "<class 'cuppak.component.button_frame.ButtonFrame'>"
    assert str(type(button._button)) == "<class 'tkinter.ttk.Button'>"

def test_button_frame_text():
    button = ButtonFrame(None, 'Test Button')
    assert button._button['text'] == 'Test Button'     

def test_button_frame_change_image():
    image_directory = os.path.dirname(os.path.abspath(__file__))
    image_path = image_directory + '\\test_image.png'

    button = ButtonFrame(None, 'Test Button', image=image_path)
    assert button._button['image']

def test_button_frame_command():
    def t_funct():
        return 863
    button = ButtonFrame(None, 'Test Button', command=t_funct)
    
    result = 0
    assert result == 0

    result = button._button.invoke()
    assert result == 863

def test_button_frame_set():
    def t_funct_a():
        return 635

    def t_funct_b():
        return 445

    button = ButtonFrame(None, 'Test Button', command=t_funct_a)
    result = button._button.invoke()
    assert result == 635

    button.set_button('Another Label', command=t_funct_b)
    result = button._button.invoke()
    assert result == 445
    assert button._button['text'] == 'Another Label'

def test_button_frame_change_child_state():
    button = ButtonFrame(None, 'Test Button')

    button.change_child_state('disabled')
    assert button._button.instate(['disabled'])

    button.change_child_state('!disabled')
    assert button._button.instate(['disabled']) == False

def test_button_frame_ttk_kwargs():
    #http://effbot.org/tkinterbook/button.htm
    #https://www.tcl.tk/man/tcl/TkCmd/ttk_button.htm#M5
    #https://docs.python.org/3/library/tkinter.ttk.html

    image_directory = os.path.dirname(os.path.abspath(__file__))
    image_path = image_directory + '\\test_image.png'

    button = ButtonFrame(None, 'Test Button', image=image_path, \
        compound='bottom', underline=0)
    assert button._button['image'] 
