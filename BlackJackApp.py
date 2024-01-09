from itertools import chain
class BlackJack:
    def __init__(self,player = 2 ,how_deck = 5):
        self.player = player
        self.deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']
        self.decks = self.deck * how_deck * 4
        self.runningCounti = 0
        self.outOfCards = []
        self.tour = self.player * 2 + 2
        self.openToursCards = []
        self.playerNames = []
        self.assignments = dict()
    def createPlayer(self):
        self.playerNames = []
        for i in range(self.player):
            player = f'{i+1}.-->>player'
            self.playerNames.append(player)
        desk = 'Desk'
        self.playerNames.append(desk)
        return self.playerNames
    def openTour(self,openTourCard):
        self.openToursCards = openTourCard
        return self.openToursCards
    def addoutplayer(self,ctr = 'none',how = 1):
        if ctr == 'add':
            self.player += how
        elif ctr == 'out':
            self.player -= how
        else:
            pass
        return self.player

    def dealCards(self):
        total_people = len(self.playerNames)
        cards_per_person = len(self.openToursCards) // total_people
    
        self.assignments = {person: [] for person in self.playerNames}
    
        for _ in range(cards_per_person):
            for person in self.playerNames:
                card = self.openToursCards.pop(0)  # Kartı listeden çıkart
                self.assignments[person].append(card)  # Kişinin eline kartı ekle
    
        return self.assignments
    
    def playersTour(self,playerName = '1.-->>player',dp ='p',card=''):
        if dp == 'd':
            self.assignments[playerName].append(card) 
        else:
            pass
        return self.assignments
    def deskTour(self,dp,card):
        desk ='Desk'
        if dp == 'd':
            self.assignments[desk].append(card)
        else:
            pass
        return self.assignments
    def qMarkCard(self,qMark):
        desk ='Desk'
        self.assignments[desk][1] = qMark 
        return self.assignments
    def endGame(self):
        self.openToursCards = []
        self.playerNames = []
        self.assignments = dict()
    def outCard(self):
        my_dict = self.assignments
        nested_list = list(my_dict.values())
        # itertools.chain kullanarak düzleştirme
        outcardsadd = list(chain.from_iterable(nested_list))
        self.outOfCards.extend(outcardsadd)
        return self.outOfCards
