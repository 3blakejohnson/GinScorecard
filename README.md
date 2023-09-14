# GinScorecard
Application to play around with Python GUI and make scoring Gin (family card game) easy

Run the app in Application.py to get started.
The GUI will prompt for number of players, then the names of each player.

Game Rules
The game is played in 7 rounds, and each round you are dealt an increasing number of cards, starting with 7 the first round, and 13 the last round.
It is played with a couple decks of playing cards mixed together (with more added as needed).
The goal is to make sets (groups of at least 3 cards of the same number) and runs (at least 4 consecutive cards of the same suit).
The goals of the rounds are as follows:
  1. 2 sets
  2. 1 set, 1 run
  3. 2 runs
  4. 3 sets
  5. 2 sets, 1 run
  6. 1 set, 2 runs
  7. 3 runs
Each turn, a player draws a card, either from the draw or discard pile.  To finish their turn, they discard a card.
After a player discards, if somebody else wants the card that was discarded, they may 'buy' it by drawing that card along with one from the draw pile.  Priority for buying cards goes to whoever's turn will come up first.

Once you have the cards in your hand to accomplish the round's goal, on your turn, you can lay them down in front of you.  At this point, you can also lay your remaining cards wherever they fit into other's 'layed-down' cards.  

The round ends when someone runs out of cards, and at this point everybody adds up their score based on the cards left in their hands:
  numbers 2-9  : 5 points
  10, J, Q, K  : 10 points
  A            : 15 points
  Joker (wild) : 25 points

The person at the end of the game with the lowest score wins.
