#card class creation
#my code runs fine without the list of values
suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def get_display_string(self):
        if self.value == 1:
            return "Ace of " + suit[self.suit-1]
        elif self.value == 11:
            return "Jack of " + suit[self.suit-1]
        elif self.value == 12:
            return "Queen of " + suit[self.suit-1]
        elif self.value == 13:
            return "King of " + suit[self.suit-1]
        else:
            return str(self.value) + " of " + suit[self.suit-1]


#####This was the first functional code I wrote
#    def get_display_string(self):
#        if self.suit == 1:
#            self.suit = "Clubs"
#        elif self.suit == 2:
#            self.suit = "Diamonds"
#        elif self.suit == 3:
#            self.suit = "Hearts"
#        else:
#            self.suit = "Spades"
#####I thought using the code below this comment would work by itself, but I kept getting numbers for self.suit instead of the names (also had to do str(self.suit) to even get it to print)
#        if self.value == 1:
#            return "Ace" + " of " + self.suit
#        elif self.value == 11:
#            return "Jack" + " of " + self.suit
#        elif self.value == 12:
#            return "Queen" + " of " + self.suit
#        elif self.value == 13:
#            return "King" + " of " + self.suit
#        else:
#            return str(self.value) + " of " + self.suit
