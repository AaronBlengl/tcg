def dropCardsFromHand(player, cards):
    for card in cards:
        if card in player.hand:
            player.hand.remove(card)
            player.graveyard.append(card)