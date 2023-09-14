"""
    Blake Johnson
    File: GinPlayer.py
    class for gin players.  Keeps track of names and scores for each round
"""


class Player(object):
    def __init__(self, name):
        self.name = name
        self.scores = [0] * 7

    def getName(self):
        return self.name

    def getScores(self):
        return self.scores

    def setScores(self, newScores):
        for i in range(0, len(self.scores)):
            self.scores[i] = newScores[i]

    def getTotal(self):
        sum = 0
        for score in self.scores:
            sum += score
        return sum

    def __str__(self):
        return str(self.name)

    def __gt__(self, other):
        if self.getTotal() > other.getTotal():
            return True
        else:
            return False

    def __lt__(self, other):
        if self.getTotal() < other.getTotal():
            return True
        else:
            return False
