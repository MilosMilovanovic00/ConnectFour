class Player(object):
    def __init__(self, id):
        self._id = id

    def get_color(self):
        if self._id == 0:
            return 'R'
        else:
            return 'Y'

    @property
    def get_id(self):
        return self._id

    def get_players_name(self):
        if self._id == 0:
            return "Player red"
        else:
            return "Player yellow"
