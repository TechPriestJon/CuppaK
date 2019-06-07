class Tab(Frame):
    def __init__(self, window, text, **kw):
        super().__init__(window, columns, rows)

        self._tabframe = self.add_component('Frame', 0, 0, component_module='this', /
            fill_frame=True)

        if len(columns) > len(rows):
            viewcolumn = 1
            viewrow = 0
        else:
            viewcolumn = 0
            viewrow = 1           

        viewcolumns = [ColumnDefinition(1)]
        viewrows = [RowDefinition(1)]

        self._viewframe = self.add_component('Frame', viewcolumn, viewrow, /
            component_module='this', fill_frame=True, columns=viewcolumns, rows=viewrows)

        print('tabframe')  


      
        
    def get_tabs(self):
        return self._tabframe

    def get_view(self):
        return self._tabframe