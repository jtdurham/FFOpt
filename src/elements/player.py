import uuid

class Player(object):
    def __init__(self):
        self.id = "P" + str(uuid.uuid4())
        self.fantasy_team = None
        self.nfl_team = None
        self.years_experience = None
        self.bye_week = None
        self.position = []
        self.drafted = False
        


