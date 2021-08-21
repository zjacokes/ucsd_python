suit = ["Club", "Diamond", "Heart", "Spade"]
value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def get_display_string(value):
        if value == 1:
            return "Ace"
        elif value == 11:
            return "Jack"
        elif value == 12:
            return "Queen"
        elif value == 13:
            return "King"
        else:
            value = str(value)
            return value
