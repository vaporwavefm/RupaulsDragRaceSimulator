# George Juarez

import collections, operator, random

# Stats will be declared as floats at the moment (5 options):
# (A) Amazing = 0.8
# (B) Great = 0.6
# (C) Average = 0.5
# (D) Bad = 0.4
# (F) Awful = 0.3

class Queen:
    def __init__(self, name, sewStat, danceStat, singStat, actStat, humorStat, lipsyncCt = 0):
        self.__name = name
        self.__sewStat = sewStat
        self.__danceStat = danceStat
        self.__singStat = singStat
        self.__actStat = actStat
        self.__humorStat = humorStat

    def get_name(self):
        return self.__name
    def get_sewStat(self):
        return self.__sewStat
    def get_danceStat(self):
        return self.__danceStat
    def get_singStat(self):
        return self.__singStat
    def get_actStat(self):
        return self.__actStat
    def get_humorStat(self):
        return self.__humorStat
    def get_lipsyncCt(self):
        return self.__lipsyncCt

    def set_name(self,name):
        self.__name = name
    def set_sewStat(sewStat):
        self.__sewStat = sewStat
    def set_danceStat(danceStat):
        self.__danceStat = danceStat
    def set_singStat(singStat):
        self.__singStat = singStat
    def set_actStat(actStat):
        self.__actStat = actStat
    def set_humorStat(humorStat):
        self.__humorStat = humorStat
    def set_lipsyncCt(lipsyncCt):
        self.__lipsyncCt = lipsyncCt

    name = property(get_name, set_name)
    sewStat = property (get_sewStat, set_sewStat)
    danceStat = property (get_danceStat, set_danceStat)
    singStat = property (get_singStat, set_singStat)
    actStat = property (get_actStat, set_actStat)
    humorStat = property (get_humorStat, set_humorStat)
    lipsyncCt = property (get_lipsyncCt, set_lipsyncCt)

#--------------------End of Queen class (yay) -----------------------------

# fuck this shit, I gotta do this I guess
class Challenge:
    def __init__(self,name,challengeType, isElim):
        self.__name = name
        self.__challengeType = challengeType
        self.__isElim = isElim

    def get_name(self):
        return self.__name
    def get_challenge_type(self):
        return self.__challengeType
    def get_isElim(self):
        return self.__isElim

    def set_name(self, name):
        self.__name = name
    def set_challenge_type(self, challengeType):
        self.__challengeType = challengeType
    def set_isElim(self, isElim):
        self.__isElim = isElim

    name = property(get_name, set_name)
    chalengeType = property(get_challenge_type, set_challenge_type)
    isElim = property(get_isElim, set_isElim)

#------------------ End of Challenge class (yay^2) -------------------------

#------------------- In order to save myself the headache -------------------
#------------------- Here is a TeamChallenge class, (subclass) --------------

class TeamChallenge(Challenge):
    def __init__(self, name, challengeType, isElim, teamCount, countIndiv):
        super(TeamChallenge,self).__init__(name,challengeType, isElim)
        self.__teamCount = teamCount
        self.__countIndiv = countIndiv

    def get_teamCount(self):
        return self.__teamCount
    def get_countIndiv(self):
        return self.__countIndiv

    def set_teamCount(self,teamCount):
        self.__teamCount = teamCount
    def set_countIndiv(self,countIndiv):
        self.__countIndiv = countIndiv

    teamCount = property(get_teamCount, set_teamCount)
    countIndiv = property(get_countIndiv, set_countIndiv)

#------------------ End of TeamChallenge class (yay^3) -----------------------

# Remember: Challenge = Name, ChallengeType, isElim

s4_challenges = [ Challenge("RuPocalypse Now!","sew", True), \
                 TeamChallenge("WTF: Wrestling Trashiest Fighters" , "humor", True, 3, [4]), \
                 TeamChallenge("Glamazons vs. Champions", "act", True, 2, [5,6]), \
                 TeamChallenge("Queens Behind Bars", "act", True, 2, [5,5]), \
                 Challenge("Snatch Game", "humor", True), \
                 Challenge("Float Your Boat", "sew", True), \
                 Challenge("Dragazines", "act", True), \
                 TeamChallenge("Frenemies", "sing", False, 3, [2,2,2]), \
                 Challenge("Frock the Vote!", "humor", True), \
                 Challenge("DILFs: Dads I'd Like To Frock", "sew", True), \
                 Challenge("The Fabulous Bitch Ball", "sew", True), \
                 Challenge("The Final Three", "none", False), \
                 Challenge("Reunited!", "none", False) ]

# Remember: Queen = Name, Sew, Dance, Sing, Act, Humor

s4_preset_contest_obj = [ Queen("Alisa Summers", 'F', 'D', 'C', 'C', 'C'), \
                          Queen("Chad Michaels", 'B', 'B', 'B', 'B', 'B'), \
                          Queen("DiDa Ritz", 'C', 'A', 'C', 'B', 'C'), \
                          Queen("Jiggly Caliente", 'F', 'A', 'C', 'C', 'B'), \
                          Queen("Lashauwn Beyond", 'A', 'D', 'C', 'B', 'C'), \
                          Queen("Latrice Royale", 'B', 'A', 'A', 'B', 'A'), \
                          Queen("Madame LaQueer", 'C', 'D', 'C', 'D', 'C'),
                          Queen("Milan", 'C', 'A', 'C', 'C', 'C'), \
                          Queen("Phi Phi O'Hara", 'B', 'A', 'B', 'C', 'B'), \
                          Queen("The Princess", 'B', 'C', 'C', 'D', 'C'), \
                          Queen("Sharon Needles", 'A', 'B', 'B', 'B', 'B'), \
                          Queen("Willam", 'B', 'B', 'A', 'A', 'A') ]

def main():
    '''
    # commented out for now

    keep_going = 'y'

    print("Hello, and welcome to the Rupaul's Drag Race simulator!", \
          "\nFor the moment, we will just be using a preset season: Season 4. \nHere are the following contestants" \
          " from Season 4 of Rupaul's Drag Race.")
    '''

    cList = mainChallenge(s4_preset_contest_obj,"humor")
    # sorted_cList will be a list of tuples sorted by the second element in each tuple
    sorted_cList = sorted(cList.items(), key = operator.itemgetter(1))
    processTopBottomSafe(sorted_cList)

    # testcList to test out the changing bounds once len(cList) < 8
    testcList = [("Jiggly Caliente", 0.444444), ("Madame LaQueer", 0.644444), ("Willam", 0.744444), \
    ("Phi Phi O'Hara",1.444444), ("DiDa Ritz", 2.444444), ("Chad Michaels", 3.444444), ("Sharon Needles", 4.44444)]
    processTopBottomSafe(testcList)

    '''
    while(keep_going.lower() == 'y'):
        print(0)
        keep_going = input("Enter y to exit: ")
    '''

def printRemaining(contest_obj):
    for i in range(0, len(contest_obj)):
        print(contest_obj.name)

def countRemaining(contest_obj):
    return len(contest_obj)

def miniChallenge(contest_obj):
    seed = random.randint(0, countRemaining(contest_obj))
    print("The winner of the mini-challenge is: ", contest_obj[seed].name, "!", sep = "")

def mainChallenge(contest_obj,challengeType):
    # So I guess the plan is to figure out a way to rank the Queens based on their performances
    # Each week, there's a certain number of Queens who are safe, and those who are on the top-bottom

    # The first thing we should do is calculate a general ranking based off the type of challenge presented this week
    queenPerformanceList = {}
    for i in range(0, countRemaining(contest_obj)):
        currentQueen = contest_obj[i]
        queenPerformanceList[currentQueen.name] = getQueenPerformance(currentQueen, challengeType)
        # Now that we have all the queen's performances for the main challenge, we should add additional points for the runway
        runwayScore = stat_to_float(currentQueen.sewStat)
        queenPerformanceList[currentQueen.name] += runwayScore
    return queenPerformanceList

def getQueenPerformance(currentQueen, challengeType):
    specifiedStat = ''
    if(challengeType == "sew"):
        specifiedStat = currentQueen.sewStat
    elif(challengeType == "dance"):
        specifiedStat = currentQueen.danceStat
    elif(challengeType == "sing"):
        specifiedStat = currentQueen.singStat
    elif(challengeType == "act"):
        specifiedStat == currentQueen.actStat
    elif(specifiedStat == "humor"):
        specifiedStat == currentQueen.humorStat
    randPerformance = random.uniform(stat_to_float(specifiedStat), stat_to_float(specifiedStat) + 1)
    return randPerformance

def stat_to_float(specifiedStat):
    return {
            'A' : 0.8,
            'B' : 0.6,
            'C' : 0.5,
            'D' : 0.4,
            'F' : 0.3,
        }.get(specifiedStat,0.0)

def processTopBottomSafe(cList):

    # REMINDER: topQueens, safeQueens, and bottomQueens are DESCENDING, so that means topQueens[0] is the winner of the challenge
    # bottomQueens[0] is "LOW" and bottomQueens[1] and bottomQueens[2] are the "BTM2"
    # safeQueens order doesn't really matter tbh

    topQueens = []
    safeQueens = []
    bottomQueens = []

    # We have to make certain cases for bounds once len(cList) < 8
    # Case 7: 4 top, 3 bottom
    # Case 6: 3 top, 3 bottom
    # Case 5: 2 top, 3 bottom
    # Case 4: 2 top, 2 bottom

    if( len(cList) >= 8 ):
        for i in range(2,-1,-1):
            bottomQueens.append(cList[i][0])
            del cList[i]
        for i in range(len(cList) - 1, len(cList) - 4, -1):
            topQueens.append(cList[i][0])
            del cList[i]
        for i in range(len(cList) - 1, -1, -1):
            safeQueens.append(cList[i][0])

        for i in range(0, len(topQueens)):
            print(topQueens[i])

        print("\n\n")

        for i in range(0, len(safeQueens)):
             print(safeQueens[i])

        print("\n\n")

        for i in range(0, len(bottomQueens)):
            print(bottomQueens[i])

    else :
        parseTopBtm = nittyGritty(len(cList))
        for i in range(parseTopBtm[1]-1, -1, -1):
            bottomQueens.append(cList[i][0])

        for i in range(len(cList) -1, len(cList) - (parseTopBtm[0] + 1), -1):
            topQueens.append(cList[i][0])

        for i in range(0, len(topQueens)):
            print(topQueens[i])

def nittyGritty(size):
    return {
        4: [2,2],
        5: [2,3],
        6: [3,3],
        7: [4,3],
    }.get(size, [2,2])

#call main
main()
