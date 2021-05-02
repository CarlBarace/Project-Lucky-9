#Lucky Nine is a card game similar to Baccarat. The object of Lucky Nine is to draw a hand that totals nine, or as closest to nine as possible. If the total of a hand exceeds nine, the value is adjusted by subtracting 10 from the total.
# The game doesn't use the faced cards King, Queen, and Jack. The game only use the cards from A to 10.

#cardDeck
import random
import time

def createDeck():
    deck = []
    for i in range(4):
        deck.append("A")
        deck.append("J")
        deck.append("Q")
        deck.append("K")
        for i in range(2, 11):
            deck.append(str(i))
    
    random.shuffle(deck)
    return deck
def playerNumber():
    print("Good day!")
    time.sleep(1)
    print("Welcome to game Lucky 9")
    time.sleep(2)
    while True:
        names = []
        players = int(input("How many of you will play the game? Min of 2/Maximum of 4 only \n"))
        if players in range(2,5):
            for player in range(players):
                nameplayer = input("What is you name, player "+ str(player+1)+ ": ")
                names.append(nameplayer.upper())
            return names
            break
        else:
            print("Min of 2/Maximum of 4 only \n")
            continue
        
def initialize(player):
    print("Okay, let's play Lucky 9.")
    time.sleep(1)
    for name in player:
        print(name + ", ", end="")
    time.sleep(1)
    print("welcome to the game, Lucky 9")
    time.sleep(1)
    rules()
    time.sleep(1)

def rules():
    print("\n Rules of the Game \n")
    print(" * No hand receives more than three cards")
    print(" * Tens and face cards (all jacks, queens and kings) are worth zero, aces are worth one, and all other cards are worth their face value")
    print(" * If the value of a hand exceeds nine, the value is adjusted by subtracting 10 from the total")
    print(" * The highest score wins \n")
    time.sleep(2)

def help():
    helper = str(input("Do you want to see the game rules? y or any key\n"))
    helper = helper.upper()
    if helper == "Y":
        rules()
    elif (helper == "--HELP"):
        done = False
        while (done == False):
            rules()
            time.sleep(1)
            back = str(input("Please enter '--return' if done\n")).upper()
            if back == "--RETURN":
                done = True
    else:
        print("You will be returning to the game. Just type --help if you want to see the rules of the game.\n")
    time.sleep(2)

class Gamer:
    # The starting amount of every player is 100
    def __init__(self, name, card = []):
        self.name = name
        self.card = card
        self.score = self.setScore()
    
    
    def __str__(self):
        show = ""
        for item in self.card:
            show += str(item) +" "
        printing = str(self.name) + ": your cards are : "+ show + " and your score is: " + str(self.score) +"\n"
        return printing
    
    def setScore(self):
        self.score = 0
        values = { "A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":0,"Q":0,"K":0,}
        for number in self.card:
            self.score += values[number]
            self.score %= 10
        return self.score

    def another(self, newCards):
        self.card = newCards
        self.score = self.setScore()
    
    def pay(self, amount):
        self.money -= amount
        self.bet += amount
    
    def win(self,result):
        if result == True:
            self.money += 2*self.bet
            self.bet =0
        else:
            self.bet = 0

def results(check):
    max = 0
    for item in check:
        if check[item] > max:
            max = check[item]
        else:
            max = max
    return max
def winner(max,check):
    flipped = {}    
    for key, value in check.items():
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key)
    (flipped[max])
    string = " "
    for item in range(len(flipped[max])):
        if item == len(flipped[max]) - 1:
            string += (flipped[max])[item]
        else:
            string += (flipped[max])[item] +" and "
    return string





cardDeck = ["J","K","Q"]
playing = playerNumber()
initialize(playing)
like = True
while (like):
    if len(cardDeck) <= 20:
        cardDeck = createDeck()
    else:
        cardDeck = cardDeck
    number = 0
    sets = {}
    for name in playing:
        print(chr(27) + "[2J") 
        print("\nIt's "+name+"'s turn.\n")
        help()
        hand = [cardDeck.pop(),cardDeck.pop()]
        name = Gamer(playing[number],hand)
        print(name)
        time.sleep(1)
        helping = True
        while (helping):
            decision = str(input(str(playing[number]) + ": Do you want to draw another card? y/ any key(no) ")) #The game only allows three cards.
            decision = decision.upper()
            print(decision)
            if decision == "Y":
                add = cardDeck.pop()
                hand.append(add)
                name = Gamer(playing[number],hand)
                time.sleep(1)
                print(name)
                helping = False
            elif (decision == "--HELP"):
                done = False
                while (done == False):
                    rules()
                    time.sleep(1)
                    back = str(input("Please enter '--return' if done\n")).upper()
                    if back == "--RETURN":
                        done = True
            else:
                time.sleep(1)
                print(name)
                helping = False    
        time.sleep(1)
        sets[playing[number]] = name.score
        number += 1

    winning = results(sets)
    checking = winner(winning,sets)
    print("The winner of this round is/are"+ str(checking)+". Go for the win. Congratulations!")
    time.sleep(3)
    want = str(input("\n\nDo you still want to play? y/any key\n"))
    want = want.upper()
    if want == "Y":
        like = True
    else:
        like = False    


