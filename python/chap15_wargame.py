# WARGAME
"""
Create the popular card game 'WAR'. In War, each player draws a card from the deck, and the player with the highest card wins. You will build War by defining classes representing a card, a deck, a player, and finally, the game itself.
"""
from random import shuffle


class Card:
    """
    spades > hearts > diamonds > clubs
    """
    suits = ["SPADES",
             "HEARTS",
             "DIAMONDS",
             "CLUBS"]

    values = [None, None,"2", "3", # 2 "None" so the string "2" in the list is at index 2
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]

    def __init__(self, v, s):
        """suit + value are ints"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        # less than; card 2
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        # greater than; card 2
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        # print card i.e. 3 of diamonds
        v = self.values[self.value] \
            + " of " + \
            self.suits[self.suit]
        return v

# from random import shuffle for class Deck
class Deck:
    def __init__(self):
        # create 52 cards - one card for every suit+value combi; 52 = ((15-2)+1)*4
        self.cards = [] # cards list
        for i in range(2, 15): # 2..10 + jack + queen + king + ace = 13; last value = 14, begin with 2; 
            for j in range(4): # 0,1,2,3 = 4 suits
                self.cards.append(Card(i,j))
        shuffle(self.cards) # randomly rearranges the items in the list "cards", mimickking the shuffling of a deck of cards

    def rm_card(self):
        # remove card from the list "cards"
        if len(self.cards) == 0: # empty list => none
            return
        return self.cards.pop() # remove the drawed card


class Player:
    def __init__(self, name):
        self.wins = 0 # how many rounds player has won
        self.card = None # card player is currently holding
        self.name = name # player name


class Game:
    def __init__(self):
        name1 = input("p1 name: ")
        name2 = input("p2 name: ")
        self.deck = Deck() # create a new deck for 2 players
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        # win a round
        w = "'{}' wins this round"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "'{}' drew {} ; '{}' drew {}" # draw
        d = d.format(p1n, # player 1's name
                     p1c, # player 1's card
                     p2n, # player 2's name
                     p2c) # player 2's card
        print(d) # print draw list

    def play_game(self):
        cards = self.deck.cards
        print("\nbeginning War!")
        while len(cards) >= 2:
            m = "\nq to quit. Any key to play: " # m = message
            response = input(m)
            if response == 'q': # quit when press "q"
                break
            p1c = self.deck.rm_card() # remove drawned card from deck
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n,
                      p1c,
                      p2n,
                      p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print("War is over. '{}' wins".format(win)) # Problem: War is over. 'It was a tie!' wins
        # all of cards has been drawned; max = 52/2 = 26 rounds

    def winner(self, p1, p2):
        # win the game
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"

game = Game()
game.play_game()
