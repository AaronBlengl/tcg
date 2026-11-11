import random

def loadDeckById(deck_id):
    # Placeholder for loading a deck from a database or file
    # This function should return a Deck object based on the provided deck_id
    pass

def shuffleDeck(player):
    random.shuffle(player.deckList)

def drawCardsfromTop(player, number=1):
    player.hand.extend(player.deckList[:number])
    player.deckList = player.deckList[number:]

def drawCardsfromBottom(player, number=1):
    player.hand.extend(player.deckList[-number:])
    player.deckList = player.deckList[:-number]

def getCardsFromDeckByType(player, card_type):
    cards = []
    for card in player.deckList:
        if card.card_type == card_type:
            cards.append(card)
    return cards

def dropSpecificCard(player, card):
    if card in player.deckList:
        player.deckList.remove(card)
        player.graveyard.append(card)

def drawSpecificCard(player, card):
    if card in player.deckList:
        player.hand.append(card)
        player.deckList.remove(card)