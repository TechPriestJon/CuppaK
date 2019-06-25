class TreeviewItemDefinition():
    def __init__(self, title, values, parent='', command=None):
        self.parent = parent
        self.title = title
        self._values = values
        self._command = command


    def get_values(self, columns):
        value_list = []
        for column in columns:
            for value in self._values:
                if column.name == value.key:
                    value_list.append(value.value)
                    continue
        
        return value_list

    def get_command(self):
        return self._command;
    