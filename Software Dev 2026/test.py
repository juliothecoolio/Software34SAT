import random

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def name(self):
        return str(self.value) + " of " + self.suit
    

class Deck():
    def __init__(self):
        self.cards = []
        suit = ["H", "D", "S", "C"]
        value =  ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        for s in suit:
            for v in value:
                self.cards.append(s + str(v))

    def shuffle(self):
        return random.shuffle(self.cards)
        
    def deal_card(self):
        card = self.cards.pop()
        return card
    
test = Deck()
print(test.cards)
test.shuffle()
print(test.cards)

print(len(test.cards))
print(test.deal_card())
print(len(test.cards))
