class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        pass

    @property
    def house(self):
        return self._house