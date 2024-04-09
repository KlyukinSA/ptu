class Role:

    @property
    def title(self):
        if not hasattr(self, '_title'):
            return None
        return self._title
    
    @title.setter
    def title(self, value: str):
        self._title = value

    @property
    def year(self):
        if not hasattr(self, '_year'):
            return None
        return self._year
    
    @year.setter
    def year(self, value: int):
        self._year = value

    @property
    def character_name(self):
        if not hasattr(self, '_character_name'):
            return None
        return self._character_name
    
    @character_name.setter
    def character_name(self, value: str):
        self._character_name = value

    @property
    def as_character(self):
        if not hasattr(self, '_as_character'):
            return None
        return self._as_character
    
    @as_character.setter
    def as_character(self, value: str):
        self._as_character = value

    @property
    def credit(self):
        if not hasattr(self, '_credit'):
            return None
        return self._credit
    
    @credit.setter
    def credit(self, value: int):
        self._credit = value

    @property
    def series_name(self):
        if not hasattr(self, '_series_name'):
            return None
        return self._series_name
    
    @series_name.setter
    def series_name(self, value: str):
        self._series_name = value

    def __init__(self) -> None:
        self.types = []

    def to_dict(self) -> dict:
        res_dict = {}
        if self.title:
            res_dict['title'] = self.title
        if self.year:
            res_dict['year'] = self.year
        if self.character_name:
            res_dict['character name'] = self.character_name
            if self.as_character:
                res_dict['character name'] = res_dict['character name'] + ' (%s)' % (self.as_character,)
        if self.series_name:
            res_dict['series_name'] = self.series_name
        if self.credit:
            res_dict['credit'] = self.credit
        for (i, type) in enumerate(self.types, 1):
            res_dict['type' + str(i)] = type
        return res_dict
