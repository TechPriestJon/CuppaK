class TreeviewDirectoryDefinition():
    def __init__(self, name, title, items=[], parent='', open=True):
        self.parent = parent
        self.name = name
        self.title = title
        self.open = open
        for item in items:
            item.parent = self.name

        self.items = items
