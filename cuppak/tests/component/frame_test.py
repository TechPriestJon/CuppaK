import pytest
from cuppak.component import *
from cuppak.dto import *

def test_frame_type():

    component_type = "<class 'cuppak.component.frame.Frame'>"
    frame = Frame(None,[],[])

    assert str(type(frame)) == component_type

def test_frame_add_component():

    columns = [ColumnDefinition(1)]
    rows = [RowDefinition(1)]
    
    frame = Frame(None,columns,rows)
    assert len(frame._components) == 0 

    component_type = "<class 'cuppak.component.dynamic_label_frame.DynamicLabelFrame'>"
    frame.add_component('DynamicLabelFrame', 0, 0, component_module='this', \
        text='Some words')
    assert len(frame._components) == 1 
    assert str(type(frame._components[0])) == component_type

def test_frame_add_component_fill_frame():

    columns = [ColumnDefinition(1)]
    rows = [RowDefinition(1)]
    
    frame = Frame(None,columns,rows)

    component_type = "<class 'cuppak.component.dynamic_label_frame.DynamicLabelFrame'>"
    label = frame.add_component('DynamicLabelFrame', 0, 0, component_module='this', \
        text='Some words', fill_frame=True)
    assert len(frame._components) == 1 
    assert str(type(frame._components[0])) == component_type
    assert label == frame._components[0]

def test_frame_add_component_tkinter():

    columns = [ColumnDefinition(1)]
    rows = [RowDefinition(1)]
    
    frame = Frame(None,columns,rows)
    assert len(frame._components) == 0 

    component_type = "<class 'tkinter.Label'>"
    label = frame.add_component('Label', 0, 0, \
        text='Some words')
    assert len(frame._components) == 1 
    assert str(type(frame._components[0])) == component_type
    assert label == frame._components[0]

def test_frame_add_component_ttk():

    columns = [ColumnDefinition(1)]
    rows = [RowDefinition(1)]
    
    frame = Frame(None,columns,rows)
    assert len(frame._components) == 0 

    component_type = "<class 'tkinter.ttk.Label'>"
    label = frame.add_component('Label', 0, 0, component_module='ttk', \
        text='Some words')
    assert len(frame._components) == 1 
    assert str(type(frame._components[0])) == component_type
    assert label == frame._components[0]

def test_frame_add_component_invalid_component():
    expected_error = "'FakeFrame' is not in list"

    columns = [ColumnDefinition(1)]
    rows = [RowDefinition(1)]
    
    frame = Frame(None,columns,rows)

    try:
        frame.add_component('FakeFrame', 0, 0, component_module='this', \
        text='Some words')
        assert False
    except ValueError as error:
        assert str(error) == expected_error

def test_frame_add_component_columns_out_of_range():
    expected_error = 'Column is outside range of screen columns'

    columns = [ColumnDefinition(1)]
    rows = [RowDefinition(1)]
    
    frame = Frame(None,columns,rows)
    assert len(frame._components) == 0 

    try:
        frame.add_component('DynamicLabelFrame', 1, 0, component_module='this', \
            text='Some words')
        assert False
    except ValueError as error:
        assert str(error) == expected_error

def test_frame_add_component_rows_out_of_range():
    expected_error = 'Row is outside range of screen rows'

    columns = [ColumnDefinition(1)]
    rows = [RowDefinition(1)]
    
    frame = Frame(None,columns,rows)
    assert len(frame._components) == 0 

    try:
        frame.add_component('DynamicLabelFrame', 0, 1, component_module='this', \
            text='Some words')
        assert False
    except ValueError as error:
        assert str(error) == expected_error

def test_frame_add_component_invalid_sticky():
    expected_error = 'Parameter sticky needs to be a string'

    columns = [ColumnDefinition(1)]
    rows = [RowDefinition(1)]
    
    frame = Frame(None,columns,rows)
    assert len(frame._components) == 0 

    try:
        frame.add_component('DynamicLabelFrame', 0, 0, component_module='this', \
            text='Some words', sticky=1)
        assert False
    except TypeError as error:
        assert str(error) == expected_error

def test_frame__change_child_state():

    columns = [ColumnDefinition(1)]
    rows = [RowDefinition(1)]
    
    frame = Frame(None,columns,rows)

    button = frame.add_component('Button', 0, 0, \
        text='Some words', fill_frame=True)
    assert len(frame._components) == 1 
    assert button == frame._components[0]
    assert button['state'] == 'normal'

    frame.change_child_state('disabled')
    assert button['state'] == 'disabled'

def test_frame__change_child_state_with_frame():

    columns = [ColumnDefinition(1)]
    rows = [RowDefinition(1)]
    
    frame = Frame(None,columns,rows)

    inner_frame = frame.add_component('Frame', 0, 0)
    assert len(frame._components) == 1 
    assert inner_frame == frame._components[0]

    frame.change_child_state('disabled')

def test_frame__change_child_state_with_scale():

    columns = [ColumnDefinition(1)]
    rows = [RowDefinition(1)]
    
    frame = Frame(None,columns,rows)

    scale = frame.add_component('Scale', 0, 0)
    assert len(frame._components) == 1 
    assert scale == frame._components[0]

    frame.change_child_state('disabled')

def test_frame__change_child_state_with_treeview():

    columns = [ColumnDefinition(1)]
    rows = [RowDefinition(1)]
    
    frame = Frame(None,columns,rows)

    treeview = frame.add_component('Treeview', 0, 0, component_module='ttk')
    assert len(frame._components) == 1 
    assert treeview == frame._components[0]

    frame.change_child_state('disabled')