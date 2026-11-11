import service.DeckService as ds
import service.HandService as hs
from model.PlayerModel import Player

testPlayer = Player()

print(testPlayer.deckList)
ds.shuffleDeck(testPlayer)
print(testPlayer.deckList)
