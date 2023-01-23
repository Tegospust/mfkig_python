
import sys



class MFKiG:
    totalcount = 0 # licznik instancji klasy

    standNum = -1
    exhibitorName = ""

    # @staticmethod
    def getTotalCount(self):
        return self.totalcount

    def __init__(self, aStandNum, anExhibitorName):
        self.standNum = aStandNum
        self.exhibitorName = anExhibitorName
        MFKiG.totalcount += 1 # przybyło 1



    def __str__(self):
        return "(%d,\"%s\")" %(self.standNum, self.exhibitorName)

    def __repr__(self):
        return "\"%d\", \"%s\" " % (self.standNum, self.exhibitorName)

    def __del__(self):
        MFKiG.totalcount += -1 # ubyło 1

        # print("MFKiG zniszczona - %s" % self.exhibitorName)

