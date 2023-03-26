class HotDrink:
    def __init__(self, name, volume):
        self._name = name
        self._volume = volume

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, new_volume):
        self._volume = new_volume

    def __str__(self):
        return f"{self._name} {self._volume}"