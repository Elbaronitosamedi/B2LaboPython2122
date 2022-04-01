import random

# Part I

class Card: 
    def __init__(self,value,color):
        self.value = value
        self.color = color

    def getValue(self):
        return self.value

    def getColor(self):
        return self.color

    def displayCard(self):
        print(self.getValue + " + " + self.getColor)


# Part II

class Cards:
    def __init__(self,listcard,countcard):
        self.listcard = listcard
        self.countcard = countcard

    def getCount(self):
        return len(self.listcard)
    
    def draw(self):
        result = self.listcard[0]
        self.listcard.pop(0)
        return result

# Part III

class Player:
    def __init__(self, hand, total,):
        self.hand = hand
        self.total = total

    def getTotal(self):
        return self.total  
    
    def addToTotal(self,value):
        royals = (11, 12, 13)
        if value > 1 and value < 11 : 
                self.total += value
        elif value in royals : 
                self.total += 10
        elif value == 1 : 
            if (self.total + 11) > 21 :
                    self.total += 1
            else :
                self.total += 11
          
    
        


def game():
    player1 = Player([],0,)
    dealer  = Player([],0,)
    deck = createDeck()

    for i in range(3) :
        card = deck.draw()
        value = card.getValue()
        if i%2 == 0:
            player1.hand.append(card)
            player1.addToTotal(value)
        else :
            dealer.hand.append(card)
            dealer.addToTotal(value)

    if (player1.getTotal() == 21) : 
        print("Blackjack ! Vous avez gagné !")


    while player1.getTotal() < 22 :
        print("votre score est de ", player1.getTotal())
        check = input("Voulez-vous tirer une carte ? (o/n)  ")
        if check == "o" : 
            card = deck.draw()
            value = card.getValue()
            player1.hand.append(card)
            player1.addToTotal(value)
            if (player1.getTotal() > 21) :
                print("Vous avez perdu")
                break
        elif check == "n":
            break
        
    while dealer.getTotal() < 16 :
        card = deck.draw()
        value = card.getValue()
        dealer.hand.append(card)
        dealer.addToTotal(value)
        print("le score de la banque est de ", dealer.getTotal())

    if (dealer.getTotal() > 21 or dealer.getTotal() < player1.getTotal() ) :
        print("Vous avez gagné")
    elif(dealer.getTotal() > player1.getTotal()) : 
        print("la banque a gagné")
   
   
   
        
def createDeck():
    colors = ('coeur', 'pique', 'trèfle', 'carreau')
    tempdeck = []
    for color in colors :
        for i in range(13) :
            tempdeck.append(Card(i, color))
    random.shuffle(tempdeck)
    deck = Cards(tempdeck, len(tempdeck))

    return deck




game()

