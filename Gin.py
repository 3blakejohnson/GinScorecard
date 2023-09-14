"""
    Blake Johnson
    GUI for Gin score keeping
"""

from breezypythongui import EasyFrame
from GinPlayer import Player


class Gin(EasyFrame):
    def __init__(self):
        self.NUM_ROUNDS = 7
        self.COL_WIDTH = 8
        EasyFrame.__init__(self, title="Gin")
        self.numPlay = int(
            self.prompterBox(title="Players", promptString="How many people will be playing?"))  # number of players
        self.players = []  # Player objects
        self.playerFields = {}  # Players info, keyed by name
        for i in range(0, self.numPlay):
            name = self.prompterBox(title="Names", promptString="Enter player number " + str(i + 1) + "'s name:")
            self.players.append(Player(name))
        self.roundsPanel = self.addPanel(row=0, column=0, columnspan=9)
        self.roundsPanel.addLabel(text="        ", row=0, column=0, sticky="NSEW")
        self.roundsPanel.addLabel(text="Round 1\n7 cards", row=0, column=1, sticky="NSEW")
        self.roundsPanel.addLabel(text="Round 2\n8 cards", row=0, column=2, sticky="NSEW")
        self.roundsPanel.addLabel(text="Round 3\n9 cards", row=0, column=3, sticky="NSEW")
        self.roundsPanel.addLabel(text="Round 4\n10 cards", row=0, column=4, sticky="NSEW")
        self.roundsPanel.addLabel(text="Round 5\n11 cards", row=0, column=5, sticky="NSEW")
        self.roundsPanel.addLabel(text="Round 6\n12 cards", row=0, column=6, sticky="NSEW")
        self.roundsPanel.addLabel(text="Round 7\n13 cards", row=0, column=7, sticky="NSEW")
        self.roundsPanel.addLabel(text="Total", row=0, column=8, sticky="NSEW")
        self.playersPanel = self.addPanel(row=1, column=0, rowspan=self.numPlay, columnspan=9)

        self.playerNames = []

        for player in self.players:
            self.playerFields[player.getName()] = []

        for i in range(0, self.numPlay):
            self.playerNames.append(self.playersPanel.addLabel(text=self.players[i].getName(), row=i, column=0))
            for num in range(0, self.NUM_ROUNDS):
                self.playerFields[self.players[i].getName()].append(
                    self.playersPanel.addIntegerField(value=self.players[i].getScores()[num], width=self.COL_WIDTH,
                                                      row=i,
                                                      column=num + 1, sticky="NSEW"))
            self.playerFields[self.players[i].getName()].append(
                self.playersPanel.addIntegerField(value=self.players[i].getTotal(), width=self.COL_WIDTH, row=i,
                                                  column=self.COL_WIDTH,
                                                  state="readonly", sticky="NSEW"))

        self.computeBtn = self.addButton(text="Compute", row=self.numPlay + 1, column=0, command=self.compute)

    def compute(self):
        """ computes total scores   """
        for i in range(0, len(self.players)):
            newScores = []
            for val in self.playerFields[self.players[i].getName()]:
                newScores.append(val.getNumber())
            self.players[i].setScores(newScores)

        self.players.sort()
        self.playersPanel.option_clear()

        for i in range(0, self.numPlay):
            self.playerNames[i]["text"] = self.players[i].getName()
            self.playerFields[self.players[i].getName()] = []
            for num in range(0, self.NUM_ROUNDS):
                self.playerFields[self.players[i].getName()].append(
                    self.playersPanel.addIntegerField(value=self.players[i].getScores()[num], width=self.COL_WIDTH,
                                                      row=i,
                                                      column=num + 1, sticky="NSEW"))
            self.playerFields[self.players[i].getName()].append(
                self.playersPanel.addIntegerField(value=self.players[i].getTotal(), width=self.COL_WIDTH, row=i,
                                                  column=self.COL_WIDTH,
                                                  state="readonly", sticky="NSEW"))
        self.playersPanel.update()
