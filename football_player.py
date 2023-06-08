class Football_player:

    def __init__(self, boots, foot, team):
        self.speed = 0
        self.height = 187
        self.boots = boots
        self.foot = foot
        self.team = team

    def kick(self):
        print("Bang! Goal! Bosh.")
    def forward(self):
        print("forward")
    def dribble(self):
        print("dribble")
